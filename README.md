# System Analizy Ryzyka Kredytowego

Kompleksowy system do analizy ryzyka kredytowego i zarządzania portfelem wierzytelności.

## Komponenty systemu

1. **Analiza Ryzyka Kredytowego**
   - Modele scoringowe
   - Klasyfikacja dłużników
   - Ocena ryzyka

2. **Modelowanie Spłat**
   - Predykcja spłat
   - Analiza historyczna
   - Kalkulatory NPV

3. **Wycena Wierzytelności**
   - Automatyczna wycena
   - Modele ryzyka-zwrotu
   - Symulacje scenariuszy

4. **Dashboardy Analityczne**
   - Wizualizacje portfela
   - Monitoring KPI
   - Raporty windykacyjne

5. **System Rezerw**
   - Kalkulacja rezerw
   - Stress-testy
   - Monitoring adekwatności

## Instalacja

```bash
pip install -r requirements.txt
```

## Struktura projektu

```
├── src/
│   ├── risk_analysis/      # System analizy ryzyka
│   ├── repayment_models/   # Modele spłat
│   ├── valuation/          # Wycena wierzytelności
│   ├── dashboards/         # Dashboardy analityczne
│   ├── provisions/         # System rezerw
│   └── utils/             # Narzędzia pomocnicze
├── tests/                 # Testy jednostkowe
├── data/                  # Przykładowe dane
└── notebooks/            # Jupyter notebooki
```

## Użycie

Szczegółowa dokumentacja każdego modułu znajduje się w odpowiednich podkatalogach. 