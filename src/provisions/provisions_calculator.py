import numpy as np
import pandas as pd
from typing import Dict, List, Optional
from sklearn.linear_model import LinearRegression
from datetime import datetime, timedelta

class ProvisionsCalculator:
    def __init__(self):
        self.provision_rates = {
            'Niskie ryzyko': 0.05,
            'Średnio-niskie ryzyko': 0.10,
            'Średnie ryzyko': 0.25,
            'Średnio-wysokie ryzyko': 0.50,
            'Wysokie ryzyko': 0.75
        }
        self.model = LinearRegression()

    def calculate_base_provisions(self,
                                portfolio: pd.DataFrame,
                                risk_categories: Dict[str, float]) -> Dict:
        """Obliczenie bazowych rezerw dla portfela."""
        provisions = {}
        total_provision = 0

        for category in self.provision_rates:
            category_amount = portfolio[portfolio['risk_category'] == category]['amount'].sum()
            provision = category_amount * self.provision_rates[category]
            provisions[category] = provision
            total_provision += provision

        return {
            'rezerwy_per_kategoria': provisions,
            'całkowita_rezerwa': total_provision,
            'wskaźnik_pokrycia': total_provision / portfolio['amount'].sum()
        }

    def adjust_for_aging(self,
                        base_provisions: float,
                        age_distribution: Dict[str, float]) -> float:
        """Korekta rezerw o strukturę wiekową portfela."""
        age_multipliers = {
            '0-30 dni': 1.0,
            '31-90 dni': 1.2,
            '91-180 dni': 1.5,
            '181-360 dni': 2.0,
            'powyżej 360 dni': 2.5
        }

        adjusted_provision = 0
        for age_bucket, amount in age_distribution.items():
            multiplier = age_multipliers.get(age_bucket, 1.0)
            adjusted_provision += amount * multiplier

        return adjusted_provision

    def calculate_expected_losses(self,
                                historical_data: pd.DataFrame,
                                forecast_period: int = 12) -> Dict:
        """Obliczenie oczekiwanych strat na podstawie danych historycznych."""
        X = historical_data[['amount', 'age', 'risk_score']]
        y = historical_data['loss']

        self.model.fit(X, y)
        
        future_losses = self.model.predict(X)
        
        return {
            'średnia_strata': np.mean(future_losses),
            'maksymalna_strata': np.max(future_losses),
            'odchylenie_standardowe': np.std(future_losses),
            'przedział_ufności': [
                np.percentile(future_losses, 5),
                np.percentile(future_losses, 95)
            ]
        }

    def perform_stress_test(self,
                          current_provisions: float,
                          portfolio_data: pd.DataFrame,
                          scenarios: List[Dict]) -> Dict:
        """Przeprowadzenie stress-testów dla rezerw."""
        results = {}
        
        for scenario in scenarios:
            stressed_provisions = current_provisions
            
            if 'default_rate_increase' in scenario:
                stressed_provisions *= (1 + scenario['default_rate_increase'])
                
            if 'recovery_rate_decrease' in scenario:
                stressed_provisions /= (1 - scenario['recovery_rate_decrease'])
                
            if 'market_downturn' in scenario:
                stressed_provisions *= (1 + scenario['market_downturn'] * 0.5)
                
            results[scenario['name']] = {
                'wymagane_rezerwy': stressed_provisions,
                'niedobór_rezerw': max(0, stressed_provisions - current_provisions),
                'wskaźnik_pokrycia': stressed_provisions / portfolio_data['amount'].sum()
            }
            
        return results

    def generate_provisions_report(self,
                                 current_state: Dict,
                                 historical_trend: pd.DataFrame,
                                 stress_test_results: Dict) -> Dict:
        """Generowanie raportu o stanie rezerw."""
        report = {
            'stan_obecny': {
                'poziom_rezerw': current_state['całkowita_rezerwa'],
                'wskaźnik_pokrycia': current_state['wskaźnik_pokrycia'],
                'struktura_rezerw': current_state['rezerwy_per_kategoria']
            },
            'analiza_trendu': self._analyze_provisions_trend(historical_trend),
            'wyniki_stress_testów': stress_test_results,
            'rekomendacje': self._generate_recommendations(current_state, stress_test_results)
        }
        
        return report

    def _analyze_provisions_trend(self, historical_data: pd.DataFrame) -> Dict:
        """Analiza trendu zmian w rezerwach."""
        trend = {
            'zmiana_roczna': (historical_data['provisions'].iloc[-1] / 
                             historical_data['provisions'].iloc[-12] - 1),
            'zmienność': historical_data['provisions'].std() / historical_data['provisions'].mean(),
            'trend_kierunek': 'wzrostowy' if historical_data['provisions'].iloc[-1] > 
                             historical_data['provisions'].iloc[-6] else 'spadkowy'
        }
        
        return trend

    def _generate_recommendations(self,
                                current_state: Dict,
                                stress_results: Dict) -> List[str]:
        """Generowanie rekomendacji dotyczących poziomu rezerw."""
        recommendations = []
        
        if current_state['wskaźnik_pokrycia'] < 0.2:
            recommendations.append("Rozważ zwiększenie poziomu rezerw - niski wskaźnik pokrycia")
            
        max_stress_impact = max(result['niedobór_rezerw'] 
                              for result in stress_results.values())
        if max_stress_impact > current_state['całkowita_rezerwa'] * 0.3:
            recommendations.append("Wysokie ryzyko w scenariuszach stresowych - " +
                                "rozważ utworzenie dodatkowego bufora")
            
        return recommendations 