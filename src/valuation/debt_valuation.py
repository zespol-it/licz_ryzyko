import numpy as np
import pandas as pd
from typing import Dict, List, Optional
from sklearn.ensemble import GradientBoostingRegressor

class DebtValuation:
    def __init__(self):
        self.model = GradientBoostingRegressor(
            n_estimators=100,
            learning_rate=0.1,
            max_depth=3
        )
        self.risk_weights = {
            'Niskie ryzyko': 1.0,
            'Średnio-niskie ryzyko': 0.8,
            'Średnie ryzyko': 0.6,
            'Średnio-wysokie ryzyko': 0.4,
            'Wysokie ryzyko': 0.2
        }

    def calculate_base_value(self, 
                           debt_amount: float,
                           age_of_debt: int,
                           risk_category: str) -> float:
        """Obliczenie bazowej wartości długu."""
        base_value = debt_amount * self.risk_weights[risk_category]
        age_discount = max(0, 1 - (age_of_debt / 60))  # 5 lat jako punkt odniesienia
        return base_value * age_discount

    def adjust_for_market_conditions(self, 
                                   base_value: float,
                                   market_factors: Dict[str, float]) -> float:
        """Korekta wartości o czynniki rynkowe."""
        market_multiplier = 1.0
        
        if 'interest_rate' in market_factors:
            market_multiplier *= (1 - market_factors['interest_rate'] * 0.1)
        
        if 'unemployment_rate' in market_factors:
            market_multiplier *= (1 - market_factors['unemployment_rate'] * 0.05)
            
        if 'gdp_growth' in market_factors:
            market_multiplier *= (1 + market_factors['gdp_growth'] * 0.1)
            
        return base_value * market_multiplier

    def calculate_recovery_probability(self,
                                    debt_features: Dict[str, float],
                                    historical_data: pd.DataFrame) -> float:
        """Obliczenie prawdopodobieństwa odzysku."""
        X = historical_data[['debt_amount', 'age', 'risk_score']]
        y = historical_data['recovered']
        
        self.model.fit(X, y)
        
        features = np.array([[
            debt_features['debt_amount'],
            debt_features['age'],
            debt_features['risk_score']
        ]])
        
        return self.model.predict_proba(features)[0][1]

    def simulate_scenarios(self,
                         base_value: float,
                         recovery_prob: float,
                         num_scenarios: int = 1000) -> Dict:
        """Symulacja scenariuszy wartości długu."""
        scenarios = np.random.normal(base_value, base_value * 0.2, num_scenarios)
        scenarios *= np.random.binomial(1, recovery_prob, num_scenarios)
        
        return {
            'expected_value': np.mean(scenarios),
            'var_95': np.percentile(scenarios, 5),
            'var_99': np.percentile(scenarios, 1),
            'max_loss': np.min(scenarios),
            'max_gain': np.max(scenarios)
        }

    def generate_pricing_recommendation(self,
                                     valuation_results: Dict,
                                     risk_appetite: float = 0.5) -> Dict:
        """Generowanie rekomendacji cenowej."""
        conservative_price = valuation_results['var_95']
        aggressive_price = valuation_results['expected_value']
        
        recommended_price = (conservative_price * (1 - risk_appetite) + 
                           aggressive_price * risk_appetite)
        
        return {
            'rekomendowana_cena': recommended_price,
            'przedział_cenowy': {
                'min': conservative_price,
                'max': aggressive_price
            },
            'uzasadnienie': self._generate_pricing_justification(valuation_results)
        }

    def _generate_pricing_justification(self, results: Dict) -> List[str]:
        """Generowanie uzasadnienia dla wyceny."""
        justification = []
        
        if results['expected_value'] > results['var_95'] * 1.5:
            justification.append("Wysoka zmienność wartości - zalecana ostrożność")
            
        if results['max_loss'] < results['expected_value'] * 0.5:
            justification.append("Znaczące ryzyko straty - rozważ zabezpieczenia")
            
        if results['max_gain'] > results['expected_value'] * 2:
            justification.append("Potencjał wysokiego zwrotu - rozważ agresywniejszą wycenę")
            
        return justification 