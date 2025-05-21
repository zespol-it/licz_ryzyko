import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from statsmodels.tsa.arima.model import ARIMA
from typing import Dict, List, Optional
import lightgbm as lgb

class RepaymentPredictor:
    def __init__(self):
        self.model = lgb.LGBMRegressor(
            objective='regression',
            n_estimators=100,
            learning_rate=0.1
        )
        self.scaler = StandardScaler()
        self.feature_columns = [
            'debt_amount',
            'months_in_default',
            'previous_payments',
            'contact_rate',
            'promises_kept_ratio',
            'income_category'
        ]

    def prepare_time_series(self, historical_data: pd.DataFrame) -> pd.DataFrame:
        """Przygotowanie szeregu czasowego spłat."""
        ts_data = historical_data.groupby('date')['payment_amount'].sum().resample('M').sum()
        return ts_data.fillna(0)

    def fit_arima_model(self, time_series: pd.Series) -> ARIMA:
        """Dopasowanie modelu ARIMA do szeregu czasowego."""
        model = ARIMA(time_series, order=(1, 1, 1))
        return model.fit()

    def predict_future_payments(self, 
                              historical_data: pd.DataFrame, 
                              forecast_periods: int = 12) -> Dict:
        """Predykcja przyszłych spłat."""
        ts_data = self.prepare_time_series(historical_data)
        arima_model = self.fit_arima_model(ts_data)
        forecast = arima_model.forecast(steps=forecast_periods)
        
        return {
            'predicted_payments': forecast.values,
            'confidence_intervals': arima_model.get_forecast(forecast_periods).conf_int()
        }

    def calculate_npv(self, 
                     future_payments: np.ndarray, 
                     discount_rate: float = 0.1) -> float:
        """Obliczenie NPV dla przewidywanych spłat."""
        periods = np.arange(1, len(future_payments) + 1)
        npv = np.sum(future_payments / (1 + discount_rate) ** periods)
        return npv

    def analyze_payment_patterns(self, historical_data: pd.DataFrame) -> Dict:
        """Analiza wzorców spłat."""
        patterns = {
            'średnia_spłata': historical_data['payment_amount'].mean(),
            'mediana_spłat': historical_data['payment_amount'].median(),
            'regularność_spłat': self._calculate_payment_regularity(historical_data),
            'sezonowość': self._detect_seasonality(historical_data)
        }
        return patterns

    def _calculate_payment_regularity(self, data: pd.DataFrame) -> float:
        """Obliczenie wskaźnika regularności spłat."""
        payment_dates = pd.to_datetime(data['payment_date'])
        intervals = payment_dates.diff().dt.days
        return 1 - (intervals.std() / intervals.mean()) if len(intervals) > 1 else 0

    def _detect_seasonality(self, data: pd.DataFrame) -> Dict:
        """Wykrywanie sezonowości w spłatach."""
        monthly_payments = data.groupby(pd.to_datetime(data['payment_date']).dt.month)['payment_amount'].mean()
        return {
            'month': monthly_payments.idxmax(),
            'relative_strength': monthly_payments.max() / monthly_payments.mean()
        }

    def generate_repayment_strategy(self, 
                                  analysis_results: Dict,
                                  risk_score: float) -> List[str]:
        """Generowanie strategii spłat."""
        strategy = []
        
        if analysis_results['regularność_spłat'] < 0.3:
            strategy.append("Wprowadź system przypomnień o płatnościach")
        
        if analysis_results['sezonowość']['relative_strength'] > 1.5:
            strategy.append(f"Zwiększ aktywność windykacyjną w miesiącu {analysis_results['sezonowość']['month']}")
        
        if risk_score > 0.7:
            strategy.append("Rozważ restrukturyzację zadłużenia")
            
        return strategy 