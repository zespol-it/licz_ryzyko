import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from typing import Dict, List, Tuple, Optional

class CreditScoring:
    def __init__(self):
        self.model = RandomForestClassifier(n_estimators=100, random_state=42)
        self.scaler = StandardScaler()
        self.feature_columns = [
            'income',
            'debt_ratio',
            'payment_history',
            'credit_history_length',
            'num_defaults',
            'employment_length'
        ]

    def prepare_features(self, data: pd.DataFrame) -> np.ndarray:
        """Przygotowanie cech do modelu."""
        features = data[self.feature_columns].copy()
        return self.scaler.fit_transform(features)

    def train_model(self, X: np.ndarray, y: np.ndarray) -> None:
        """Trenowanie modelu scoringowego."""
        self.model.fit(X, y)

    def predict_risk_score(self, features: np.ndarray) -> np.ndarray:
        """Predykcja score'u ryzyka."""
        probabilities = self.model.predict_proba(features)
        return probabilities[:, 1]  # Prawdopodobieństwo defaultu

    def calculate_risk_category(self, score: float) -> str:
        """Określenie kategorii ryzyka na podstawie score'u."""
        if score < 0.2:
            return "Niskie ryzyko"
        elif score < 0.4:
            return "Średnio-niskie ryzyko"
        elif score < 0.6:
            return "Średnie ryzyko"
        elif score < 0.8:
            return "Średnio-wysokie ryzyko"
        else:
            return "Wysokie ryzyko"

    def evaluate_portfolio(self, portfolio: pd.DataFrame) -> Dict:
        """Ocena całego portfela."""
        features = self.prepare_features(portfolio)
        scores = self.predict_risk_score(features)
        
        return {
            'średni_score': np.mean(scores),
            'mediana_score': np.median(scores),
            'rozkład_kategorii': {
                cat: np.sum([self.calculate_risk_category(s) == cat for s in scores])
                for cat in ["Niskie ryzyko", "Średnio-niskie ryzyko", "Średnie ryzyko", 
                          "Średnio-wysokie ryzyko", "Wysokie ryzyko"]
            }
        }

    def generate_risk_report(self, portfolio: pd.DataFrame) -> Dict:
        """Generowanie raportu ryzyka."""
        eval_results = self.evaluate_portfolio(portfolio)
        features = self.prepare_features(portfolio)
        scores = self.predict_risk_score(features)

        return {
            'podsumowanie_portfela': eval_results,
            'wskaźniki_ryzyka': {
                'var_95': np.percentile(scores, 95),
                'expected_loss': np.mean(scores) * portfolio['amount'].sum(),
                'risk_concentration': np.sum(scores > 0.8) / len(scores)
            },
            'rekomendacje': self._generate_recommendations(eval_results)
        }

    def _generate_recommendations(self, eval_results: Dict) -> List[str]:
        """Generowanie rekomendacji na podstawie wyników."""
        recommendations = []
        if eval_results['średni_score'] > 0.6:
            recommendations.append("Rozważ zaostrzenie kryteriów akceptacji")
        if eval_results['rozkład_kategorii']['Wysokie ryzyko'] > 0.2:
            recommendations.append("Konieczne działania mitygacyjne dla wysokiego ryzyka")
        return recommendations 