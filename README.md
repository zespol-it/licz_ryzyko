# System Oceny Ryzyka Kredytowego / Credit Risk Assessment System

[English version below](#english-version)

## Spis treści
1. [O projekcie](#o-projekcie)
2. [Dokumentacja](#dokumentacja)
3. [Wymagania](#wymagania)
4. [Instalacja](#instalacja)
5. [Struktura projektu](#struktura-projektu)
6. [Licencja](#licencja)

## O projekcie
System kompleksowej oceny ryzyka kredytowego wykorzystujący zaawansowane algorytmy i uczenie maszynowe do analizy i oceny ryzyka. System wspiera proces decyzyjny w zakresie przyznawania kredytów i zarządzania ryzykiem portfela.

### Główne komponenty
- **System Analizy Ryzyka Kredytowego**
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

## Dokumentacja

### Dla użytkowników
- [Przewodnik użytkownika (PL)](docs/USER_GUIDE_PL.md)
- [User Guide (EN)](docs/USER_GUIDE_EN.md)

### Dla deweloperów
- [Dokumentacja techniczna (PL)](docs/TECHNICAL_GUIDE_PL.md)
- [Technical Documentation (EN)](docs/TECHNICAL_GUIDE_EN.md)

## Wymagania
- Python 3.8+
- PostgreSQL 13+
- Zależności Python:
  ```
  pandas >= 2.0.3
  numpy >= 1.24.3
  scikit-learn >= 1.3.0
  sqlalchemy >= 2.0.0
  tensorflow >= 2.13.0
  pytorch >= 2.0.0
  ```

## Instalacja
```bash
# Klonowanie repozytorium
git clone https://github.com/your-repo/licz_ryzyko

# Przejście do katalogu projektu
cd licz_ryzyko

# Utworzenie i aktywacja środowiska wirtualnego
python -m venv venv
source venv/bin/activate  # Linux/MacOS
# lub
.\venv\Scripts\activate  # Windows

# Instalacja zależności
pip install -r requirements.txt

# Konfiguracja bazy danych
python scripts/setup_database.py

# Uruchomienie testów
python -m pytest tests/
```

## Struktura projektu
```
licz_ryzyko/
├── docs/                    # Dokumentacja
│   ├── USER_GUIDE_PL.md    # Przewodnik użytkownika (PL)
│   ├── USER_GUIDE_EN.md    # User Guide (EN)
│   ├── TECHNICAL_GUIDE_PL.md # Dokumentacja techniczna (PL)
│   └── TECHNICAL_GUIDE_EN.md # Technical Documentation (EN)
├── src/                     # Kod źródłowy
│   ├── risk_assessment/    # Moduł oceny ryzyka
│   ├── ai_agent/          # Agent AI
│   ├── api/               # API systemu
│   └── utils/             # Narzędzia pomocnicze
├── tests/                  # Testy
├── scripts/                # Skrypty pomocnicze
├── requirements.txt        # Zależności projektu
└── README.md              # Ten plik
```

## Licencja
MIT License

---

# English Version

## Table of Contents
1. [About](#about)
2. [Documentation](#documentation)
3. [Requirements](#requirements)
4. [Installation](#installation)
5. [Project Structure](#project-structure)
6. [License](#license)

## About
A comprehensive credit risk assessment system utilizing advanced algorithms and machine learning for risk analysis and evaluation. The system supports decision-making in credit granting and portfolio risk management.

### Main Components
- **Credit Risk Analysis System**
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

## Documentation

### For Users
- [User Guide (EN)](docs/USER_GUIDE_EN.md)
- [Przewodnik użytkownika (PL)](docs/USER_GUIDE_PL.md)

### For Developers
- [Technical Documentation (EN)](docs/TECHNICAL_GUIDE_EN.md)
- [Dokumentacja techniczna (PL)](docs/TECHNICAL_GUIDE_PL.md)

## Requirements
- Python 3.8+
- PostgreSQL 13+
- Python dependencies:
  ```
  pandas >= 2.0.3
  numpy >= 1.24.3
  scikit-learn >= 1.3.0
  sqlalchemy >= 2.0.0
  tensorflow >= 2.13.0
  pytorch >= 2.0.0
  ```

## Installation
```bash
# Clone repository
git clone https://github.com/your-repo/licz_ryzyko

# Navigate to project directory
cd licz_ryzyko

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # Linux/MacOS
# or
.\venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Configure database
python scripts/setup_database.py

# Run tests
python -m pytest tests/
```

## Project Structure
```
licz_ryzyko/
├── docs/                    # Documentation
│   ├── USER_GUIDE_EN.md    # User Guide (EN)
│   ├── USER_GUIDE_PL.md    # User Guide (PL)
│   ├── TECHNICAL_GUIDE_EN.md # Technical Documentation (EN)
│   └── TECHNICAL_GUIDE_PL.md # Technical Documentation (PL)
├── src/                     # Source code
│   ├── risk_assessment/    # Risk assessment module
│   ├── ai_agent/          # AI Agent
│   ├── api/               # System API
│   └── utils/             # Utility tools
├── tests/                  # Tests
├── scripts/                # Helper scripts
├── requirements.txt        # Project dependencies
└── README.md              # This file
```

## License
MIT License 