# System Oceny Ryzyka Kredytowego / Credit Risk Assessment System

[English version below](#english-version)

## Spis treści
1. [O projekcie](#o-projekcie)
2. [Funkcjonalności](#funkcjonalności)
3. [Wymagania](#wymagania)
4. [Instalacja](#instalacja)
5. [Użycie](#użycie)
6. [Dokumentacja](#dokumentacja)
7. [Licencja](#licencja)

## O projekcie
System kompleksowej oceny ryzyka kredytowego wykorzystujący zaawansowane algorytmy i uczenie maszynowe do analizy i oceny ryzyka. System wspiera proces decyzyjny w zakresie przyznawania kredytów i zarządzania ryzykiem portfela.

## Funkcjonalności
- **Analiza Ryzyka Kredytowego**
  - Scoring kredytowy
  - Ocena zdolności kredytowej
  - Analiza historii kredytowej
  
- **Modelowanie Spłat**
  - Prognozowanie zachowań płatniczych
  - Analiza prawdopodobieństwa defaultu
  - Modelowanie przepływów pieniężnych

- **System Wyceny Długu**
  - Kalkulacja wartości zabezpieczeń
  - Wycena portfela kredytowego
  - Analiza LTV (Loan-to-Value)

- **Dashboardy Analityczne**
  - Interaktywne wizualizacje
  - Raporty w czasie rzeczywistym
  - Kluczowe wskaźniki efektywności (KPI)

- **System Zarządzania Rezerwami**
  - Kalkulacja rezerw
  - Testy warunków skrajnych
  - Prognozowanie potrzeb kapitałowych

## Wymagania
- Python 3.8+
- Pandas >= 2.0.3
- NumPy >= 1.24.3
- Scikit-learn >= 1.3.0
- SQLAlchemy
- R (opcjonalnie)

## Instalacja
```bash
# Klonowanie repozytorium
git clone https://github.com/your-repo/licz_ryzyko

# Przejście do katalogu projektu
cd licz_ryzyko

# Instalacja zależności
pip install -r requirements.txt

# Uruchomienie testów
python -m pytest tests/
```

## Użycie
```python
from risk_assessment import RiskAnalyzer

# Inicjalizacja analizatora
analyzer = RiskAnalyzer()

# Analiza ryzyka
risk_score = analyzer.calculate_risk({
    'financial_statement': financial_data,
    'credit_history': credit_data,
    'income_statement': income_data
})

# Generowanie rekomendacji
recommendations = analyzer.generate_recommendations(risk_score)
```

## Dokumentacja
Szczegółowa dokumentacja dostępna jest w następujących plikach:
- [Dokumentacja podstawowa](docs/DOCUMENT_RISK_AGENT.md)
- [Dokumentacja agenta AI](docs/AI_AGENT_DOCUMENTATION.md)

## Licencja
MIT License

---

# English Version

## Table of Contents
1. [About](#about)
2. [Features](#features)
3. [Requirements](#requirements)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Documentation](#documentation)
7. [License](#license)

## About
A comprehensive credit risk assessment system utilizing advanced algorithms and machine learning for risk analysis and evaluation. The system supports decision-making in credit granting and portfolio risk management.

## Features
- **Credit Risk Analysis**
  - Credit scoring
  - Creditworthiness assessment
  - Credit history analysis
  
- **Repayment Modeling**
  - Payment behavior forecasting
  - Default probability analysis
  - Cash flow modeling

- **Debt Valuation System**
  - Collateral valuation
  - Credit portfolio valuation
  - LTV (Loan-to-Value) analysis

- **Analytical Dashboards**
  - Interactive visualizations
  - Real-time reporting
  - Key Performance Indicators (KPIs)

- **Provisions Management System**
  - Provisions calculation
  - Stress testing
  - Capital requirements forecasting

## Requirements
- Python 3.8+
- Pandas >= 2.0.3
- NumPy >= 1.24.3
- Scikit-learn >= 1.3.0
- SQLAlchemy
- R (optional)

## Installation
```bash
# Clone repository
git clone https://github.com/your-repo/licz_ryzyko

# Navigate to project directory
cd licz_ryzyko

# Install dependencies
pip install -r requirements.txt

# Run tests
python -m pytest tests/
```

## Usage
```python
from risk_assessment import RiskAnalyzer

# Initialize analyzer
analyzer = RiskAnalyzer()

# Risk analysis
risk_score = analyzer.calculate_risk({
    'financial_statement': financial_data,
    'credit_history': credit_data,
    'income_statement': income_data
})

# Generate recommendations
recommendations = analyzer.generate_recommendations(risk_score)
```

## Documentation
Detailed documentation is available in the following files:
- [Basic Documentation](docs/DOCUMENT_RISK_AGENT.md)
- [AI Agent Documentation](docs/AI_AGENT_DOCUMENTATION.md)

## License
MIT License 