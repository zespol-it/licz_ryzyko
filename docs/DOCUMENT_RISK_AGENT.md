# Agent Weryfikacji Dokumentów i Oceny Ryzyka

## Spis treści
1. [Wprowadzenie](#wprowadzenie)
2. [Wymagane dokumenty](#wymagane-dokumenty)
3. [Proces weryfikacji](#proces-weryfikacji)
4. [Ocena ryzyka](#ocena-ryzyka)
5. [Przykład użycia](#przykład-użycia)

## Wprowadzenie

Agent służy do automatycznej weryfikacji dokumentów i oceny ryzyka kredytowego. System:
- Sprawdza kompletność i poprawność dostarczonych dokumentów
- Waliduje zawartość każdego dokumentu
- Oblicza scoring ryzyka na podstawie analizy dokumentów
- Generuje rekomendacje

## Wymagane dokumenty

### Dokumenty obowiązkowe:

1. **Sprawozdanie finansowe**
   - assets (aktywa)
   - liabilities (zobowiązania)
   - revenue (przychody)
   - profit (zysk)

2. **Zaświadczenie o dochodach**
   - monthly_income (miesięczny dochód)
   - employment_period (okres zatrudnienia)
   - position (stanowisko)

3. **Umowa o pracę**
   - contract_type (typ umowy)
   - start_date (data rozpoczęcia)
   - salary (wynagrodzenie)

4. **Historia kredytowa**
   - credit_score (scoring kredytowy)
   - payment_history (historia płatności)
   - active_loans (aktywne kredyty)

### Dokumenty opcjonalne:

5. **Wycena majątku**
   - property_value (wartość nieruchomości)
   - valuation_date (data wyceny)
   - property_type (typ nieruchomości)

## Proces weryfikacji

### 1. Walidacja dokumentów
```python
from agents.document_risk_agent import DocumentRiskAgent

agent = DocumentRiskAgent()
validated_docs = agent.validate_documents(documents)
```

System sprawdza:
- Czy dostarczono wszystkie wymagane dokumenty
- Czy dokumenty zawierają wszystkie wymagane pola
- Poprawność formatu danych

### 2. Struktura dokumentów

Dokumenty należy dostarczyć w formie słownika:
```python
documents = {
    'financial_statement': {
        'assets': 1000000,
        'liabilities': 300000,
        'revenue': 500000,
        'profit': 100000
    },
    'income_statement': {
        'monthly_income': 8000,
        'employment_period': 36,
        'position': 'Senior Specialist'
    },
    # ... pozostałe dokumenty
}
```

## Ocena ryzyka

### Komponenty oceny:

1. **Stabilność finansowa** (30%)
   - Wskaźnik zadłużenia
   - Marża zysku

2. **Wiarygodność dochodów** (25%)
   - Wysokość dochodów
   - Stabilność zatrudnienia

3. **Stabilność zatrudnienia** (20%)
   - Typ umowy
   - Okres zatrudnienia

4. **Historia kredytowa** (15%)
   - Scoring kredytowy
   - Historia spłat

5. **Majątek** (10%)
   - Wartość nieruchomości
   - Inne aktywa

### Kategorie ryzyka:

- Niskie ryzyko (≥ 0.8)
- Średnio-niskie ryzyko (≥ 0.6)
- Średnie ryzyko (≥ 0.4)
- Średnio-wysokie ryzyko (≥ 0.2)
- Wysokie ryzyko (< 0.2)

## Przykład użycia

```python
from agents.document_risk_agent import DocumentRiskAgent

# Inicjalizacja agenta
agent = DocumentRiskAgent()

# Przygotowanie dokumentów
documents = {
    'financial_statement': {
        'assets': 1000000,
        'liabilities': 300000,
        'revenue': 500000,
        'profit': 100000
    },
    'income_statement': {
        'monthly_income': 8000,
        'employment_period': 36,
        'position': 'Senior Specialist'
    },
    'employment_contract': {
        'contract_type': 'permanent',
        'start_date': '2020-01-01',
        'salary': 8000
    },
    'credit_history': {
        'credit_score': 0.85,
        'payment_history': 0.95,
        'active_loans': 1
    }
}

# Walidacja dokumentów
validated_docs = agent.validate_documents(documents)

# Sprawdzenie wyników walidacji
for doc_key, doc in validated_docs.items():
    print(f"{doc.name}:")
    print(f"  - Dostarczony: {doc.provided}")
    print(f"  - Status walidacji: {doc.validation_status}")
    print(f"  - Komunikat: {doc.validation_message}")

# Obliczenie ryzyka
risk_assessment = agent.calculate_risk_score(validated_docs)

# Analiza wyników
print("\nWynik oceny ryzyka:")
print(f"Status: {risk_assessment['status']}")
if risk_assessment['status'] == 'success':
    print(f"Ogólny scoring: {risk_assessment['overall_score']:.2f}")
    print(f"Kategoria ryzyka: {risk_assessment['risk_category']}")
    print("\nOceny składowe:")
    for component, score in risk_assessment['components'].items():
        print(f"- {component}: {score:.2f}")
    print("\nRekomendacje:")
    for rec in risk_assessment['recommendations']:
        print(f"- {rec}")
else:
    print(f"Błąd: {risk_assessment['message']}")
    print("Brakujące dokumenty:")
    for doc in risk_assessment['missing_documents']:
        print(f"- {doc}")
```

### Przykładowy wynik:

```python
{
    'status': 'success',
    'overall_score': 0.75,
    'risk_category': 'Średnio-niskie ryzyko',
    'components': {
        'financial_stability': 0.82,
        'income_reliability': 0.73,
        'employment_stability': 0.90,
        'credit_history': 0.88,
        'assets': 0.50
    },
    'recommendations': [
        "Rozważ dodatkowe zabezpieczenie majątkowe"
    ]
}
``` 