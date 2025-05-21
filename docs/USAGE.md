# Dokumentacja użytkowania systemu

## Spis treści
1. [Analiza Ryzyka Kredytowego](#analiza-ryzyka-kredytowego)
2. [Modelowanie Spłat](#modelowanie-spłat)
3. [Wycena Wierzytelności](#wycena-wierzytelności)
4. [Dashboard Analityczny](#dashboard-analityczny)
5. [System Rezerw](#system-rezerw)

## Analiza Ryzyka Kredytowego

```python
from risk_analysis.credit_scoring import CreditScoring
import pandas as pd

# Inicjalizacja modelu
scoring = CreditScoring()

# Przykładowe dane
data = pd.DataFrame({
    'income': [5000, 3000, 8000],
    'debt_ratio': [0.3, 0.6, 0.2],
    'payment_history': [0.95, 0.7, 0.9],
    'credit_history_length': [60, 24, 120],
    'num_defaults': [0, 2, 0],
    'employment_length': [36, 12, 84],
    'amount': [10000, 5000, 15000]
})

# Ocena ryzyka dla portfela
portfolio_evaluation = scoring.evaluate_portfolio(data)
print("Ocena portfela:", portfolio_evaluation)

# Generowanie raportu ryzyka
risk_report = scoring.generate_risk_report(data)
print("Raport ryzyka:", risk_report)
```

## Modelowanie Spłat

```python
from repayment_models.repayment_predictor import RepaymentPredictor
import pandas as pd

# Inicjalizacja predyktora
predictor = RepaymentPredictor()

# Przykładowe dane historyczne
historical_data = pd.DataFrame({
    'date': pd.date_range(start='2023-01-01', periods=12, freq='M'),
    'payment_amount': [1000, 1200, 800, 1500, 1100, 900, 1300, 1400, 1000, 1200, 1100, 1300],
    'payment_date': pd.date_range(start='2023-01-01', periods=12, freq='M')
})

# Predykcja przyszłych spłat
future_payments = predictor.predict_future_payments(historical_data, forecast_periods=6)
print("Prognoza spłat:", future_payments)

# Analiza wzorców spłat
patterns = predictor.analyze_payment_patterns(historical_data)
print("Wzorce spłat:", patterns)

# Obliczenie NPV
npv = predictor.calculate_npv(future_payments['predicted_payments'], discount_rate=0.1)
print("NPV:", npv)
```

## Wycena Wierzytelności

```python
from valuation.debt_valuation import DebtValuation
import pandas as pd

# Inicjalizacja modelu wyceny
valuation = DebtValuation()

# Przykładowe parametry długu
debt_params = {
    'debt_amount': 10000,
    'age_of_debt': 12,  # miesiące
    'risk_category': 'Średnie ryzyko'
}

# Obliczenie bazowej wartości
base_value = valuation.calculate_base_value(
    debt_amount=debt_params['debt_amount'],
    age_of_debt=debt_params['age_of_debt'],
    risk_category=debt_params['risk_category']
)

# Korekta o warunki rynkowe
market_factors = {
    'interest_rate': 0.05,
    'unemployment_rate': 0.06,
    'gdp_growth': 0.03
}
adjusted_value = valuation.adjust_for_market_conditions(base_value, market_factors)

# Symulacja scenariuszy
scenarios = valuation.simulate_scenarios(
    base_value=adjusted_value,
    recovery_prob=0.7,
    num_scenarios=1000
)

# Generowanie rekomendacji cenowej
pricing = valuation.generate_pricing_recommendation(scenarios, risk_appetite=0.5)
print("Rekomendacja cenowa:", pricing)
```

## Dashboard Analityczny

```python
from dashboards.main_dashboard import RiskDashboard

# Inicjalizacja i uruchomienie dashboardu
dashboard = RiskDashboard()
dashboard.run_server(debug=True, port=8050)

# Dashboard będzie dostępny pod adresem http://localhost:8050
```

## System Rezerw

```python
from provisions.provisions_calculator import ProvisionsCalculator
import pandas as pd

# Inicjalizacja kalkulatora rezerw
calculator = ProvisionsCalculator()

# Przykładowe dane portfela
portfolio_data = pd.DataFrame({
    'amount': [10000, 20000, 15000, 25000],
    'risk_category': ['Niskie ryzyko', 'Średnie ryzyko', 'Wysokie ryzyko', 'Średnio-niskie ryzyko'],
    'age': [30, 90, 180, 60]
})

# Obliczenie bazowych rezerw
risk_categories = {cat: 1.0 for cat in calculator.provision_rates.keys()}
base_provisions = calculator.calculate_base_provisions(portfolio_data, risk_categories)

# Korekta o strukturę wiekową
age_distribution = {
    '0-30 dni': 10000,
    '31-90 dni': 20000,
    '91-180 dni': 15000,
    '181-360 dni': 5000
}
adjusted_provisions = calculator.adjust_for_aging(
    base_provisions['całkowita_rezerwa'],
    age_distribution
)

# Przeprowadzenie stress-testów
stress_scenarios = [
    {'name': 'Umiarkowany', 'default_rate_increase': 0.1, 'recovery_rate_decrease': 0.1},
    {'name': 'Poważny', 'default_rate_increase': 0.2, 'recovery_rate_decrease': 0.2, 'market_downturn': 0.15}
]
stress_results = calculator.perform_stress_test(
    adjusted_provisions,
    portfolio_data,
    stress_scenarios
)

# Generowanie raportu
historical_trend = pd.DataFrame({
    'date': pd.date_range(start='2023-01-01', periods=24, freq='M'),
    'provisions': range(1000000, 1240000, 10000)
})
report = calculator.generate_provisions_report(
    current_state=base_provisions,
    historical_trend=historical_trend,
    stress_test_results=stress_results
)
print("Raport rezerw:", report)
```

## Przykład integracji wszystkich komponentów

```python
# Inicjalizacja wszystkich komponentów
scoring = CreditScoring()
predictor = RepaymentPredictor()
valuation = DebtValuation()
calculator = ProvisionsCalculator()
dashboard = RiskDashboard()

# Analiza nowego długu
def analyze_new_debt(debt_data: pd.DataFrame):
    # 1. Ocena ryzyka
    risk_score = scoring.predict_risk_score(debt_data)
    risk_category = scoring.calculate_risk_category(risk_score)
    
    # 2. Prognoza spłat
    payment_forecast = predictor.predict_future_payments(debt_data)
    
    # 3. Wycena
    base_value = valuation.calculate_base_value(
        debt_amount=debt_data['amount'].sum(),
        age_of_debt=debt_data['age'].mean(),
        risk_category=risk_category
    )
    
    # 4. Kalkulacja rezerw
    provisions = calculator.calculate_base_provisions(
        debt_data,
        {risk_category: 1.0}
    )
    
    return {
        'ryzyko': risk_score,
        'kategoria': risk_category,
        'prognoza_splat': payment_forecast,
        'wycena': base_value,
        'rezerwy': provisions
    }

# Przykład użycia
if __name__ == '__main__':
    # Uruchomienie dashboardu
    dashboard.run_server(debug=True) 