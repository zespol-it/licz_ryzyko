import pandas as pd
import numpy as np
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass
from datetime import datetime

@dataclass
class Document:
    name: str
    type: str
    content: dict
    required: bool
    provided: bool = False
    validation_status: bool = False
    validation_message: str = ""

class DocumentRiskAgent:
    def __init__(self):
        self.required_documents = {
            'financial_statement': Document(
                name="Sprawozdanie finansowe",
                type="financial",
                content={},
                required=True
            ),
            'income_statement': Document(
                name="Zaświadczenie o dochodach",
                type="income",
                content={},
                required=True
            ),
            'employment_contract': Document(
                name="Umowa o pracę",
                type="employment",
                content={},
                required=True
            ),
            'credit_history': Document(
                name="Historia kredytowa",
                type="credit",
                content={},
                required=True
            ),
            'property_valuation': Document(
                name="Wycena majątku",
                type="property",
                content={},
                required=False
            )
        }
        
        self.risk_weights = {
            'financial_stability': 0.3,
            'income_reliability': 0.25,
            'employment_stability': 0.2,
            'credit_history': 0.15,
            'assets': 0.1
        }

    def validate_documents(self, provided_documents: Dict[str, dict]) -> Dict[str, Document]:
        """Sprawdzenie kompletności i poprawności dokumentów."""
        validation_results = self.required_documents.copy()
        
        for doc_key, doc_content in provided_documents.items():
            if doc_key in validation_results:
                doc = validation_results[doc_key]
                doc.provided = True
                doc.content = doc_content
                
                # Walidacja specyficzna dla typu dokumentu
                validation_status, message = self._validate_document_content(doc)
                doc.validation_status = validation_status
                doc.validation_message = message
                
                validation_results[doc_key] = doc
        
        return validation_results

    def _validate_document_content(self, document: Document) -> Tuple[bool, str]:
        """Walidacja zawartości dokumentu."""
        if document.type == "financial":
            return self._validate_financial_statement(document.content)
        elif document.type == "income":
            return self._validate_income_statement(document.content)
        elif document.type == "employment":
            return self._validate_employment_contract(document.content)
        elif document.type == "credit":
            return self._validate_credit_history(document.content)
        elif document.type == "property":
            return self._validate_property_valuation(document.content)
        
        return False, "Nieznany typ dokumentu"

    def _validate_financial_statement(self, content: dict) -> Tuple[bool, str]:
        required_fields = ['assets', 'liabilities', 'revenue', 'profit']
        return self._check_required_fields(content, required_fields)

    def _validate_income_statement(self, content: dict) -> Tuple[bool, str]:
        required_fields = ['monthly_income', 'employment_period', 'position']
        return self._check_required_fields(content, required_fields)

    def _validate_employment_contract(self, content: dict) -> Tuple[bool, str]:
        required_fields = ['contract_type', 'start_date', 'salary']
        return self._check_required_fields(content, required_fields)

    def _validate_credit_history(self, content: dict) -> Tuple[bool, str]:
        required_fields = ['credit_score', 'payment_history', 'active_loans']
        return self._check_required_fields(content, required_fields)

    def _validate_property_valuation(self, content: dict) -> Tuple[bool, str]:
        required_fields = ['property_value', 'valuation_date', 'property_type']
        return self._check_required_fields(content, required_fields)

    def _check_required_fields(self, content: dict, required_fields: List[str]) -> Tuple[bool, str]:
        """Sprawdzenie czy wszystkie wymagane pola są obecne."""
        missing_fields = [field for field in required_fields if field not in content]
        
        if missing_fields:
            return False, f"Brakujące pola: {', '.join(missing_fields)}"
        return True, "Dokument poprawny"

    def calculate_risk_score(self, validated_documents: Dict[str, Document]) -> Dict:
        """Obliczenie scoringu ryzyka na podstawie dokumentów."""
        if not self._check_required_documents(validated_documents):
            return {
                'status': 'error',
                'message': 'Brak wymaganych dokumentów',
                'missing_documents': self._get_missing_documents(validated_documents)
            }

        risk_components = {
            'financial_stability': self._assess_financial_stability(validated_documents),
            'income_reliability': self._assess_income_reliability(validated_documents),
            'employment_stability': self._assess_employment_stability(validated_documents),
            'credit_history': self._assess_credit_history(validated_documents),
            'assets': self._assess_assets(validated_documents)
        }

        weighted_score = sum(
            score * self.risk_weights[component]
            for component, score in risk_components.items()
        )

        risk_category = self._determine_risk_category(weighted_score)
        
        return {
            'status': 'success',
            'overall_score': weighted_score,
            'risk_category': risk_category,
            'components': risk_components,
            'recommendations': self._generate_recommendations(risk_components)
        }

    def _check_required_documents(self, documents: Dict[str, Document]) -> bool:
        """Sprawdzenie czy wszystkie wymagane dokumenty są dostarczone i poprawne."""
        for doc in documents.values():
            if doc.required and (not doc.provided or not doc.validation_status):
                return False
        return True

    def _get_missing_documents(self, documents: Dict[str, Document]) -> List[str]:
        """Lista brakujących lub niepoprawnych dokumentów."""
        missing = []
        for doc_key, doc in documents.items():
            if doc.required and (not doc.provided or not doc.validation_status):
                missing.append(doc.name)
        return missing

    def _assess_financial_stability(self, documents: Dict[str, Document]) -> float:
        """Ocena stabilności finansowej."""
        financial_doc = documents['financial_statement'].content
        
        assets = financial_doc.get('assets', 0)
        liabilities = financial_doc.get('liabilities', 0)
        revenue = financial_doc.get('revenue', 0)
        profit = financial_doc.get('profit', 0)

        if assets == 0 or revenue == 0:
            return 0.0

        debt_ratio = liabilities / assets
        profit_margin = profit / revenue
        
        score = (1 - min(debt_ratio, 1)) * 0.6 + max(min(profit_margin, 1), 0) * 0.4
        return score

    def _assess_income_reliability(self, documents: Dict[str, Document]) -> float:
        """Ocena wiarygodności dochodów."""
        income_doc = documents['income_statement'].content
        
        monthly_income = income_doc.get('monthly_income', 0)
        employment_period = income_doc.get('employment_period', 0)
        
        income_score = min(monthly_income / 10000, 1)  # Normalizacja do 10000
        period_score = min(employment_period / 60, 1)  # Normalizacja do 5 lat
        
        return income_score * 0.7 + period_score * 0.3

    def _assess_employment_stability(self, documents: Dict[str, Document]) -> float:
        """Ocena stabilności zatrudnienia."""
        employment_doc = documents['employment_contract'].content
        
        contract_type = employment_doc.get('contract_type', '')
        contract_scores = {
            'permanent': 1.0,
            'fixed_term': 0.7,
            'b2b': 0.6,
            'temporary': 0.4
        }
        
        return contract_scores.get(contract_type, 0.0)

    def _assess_credit_history(self, documents: Dict[str, Document]) -> float:
        """Ocena historii kredytowej."""
        credit_doc = documents['credit_history'].content
        
        credit_score = credit_doc.get('credit_score', 0)
        payment_history = credit_doc.get('payment_history', 0)
        
        return (credit_score * 0.6 + payment_history * 0.4)

    def _assess_assets(self, documents: Dict[str, Document]) -> float:
        """Ocena majątku."""
        if 'property_valuation' not in documents or not documents['property_valuation'].provided:
            return 0.5  # Neutralna ocena jeśli brak dokumentu
            
        property_doc = documents['property_valuation'].content
        property_value = property_doc.get('property_value', 0)
        
        return min(property_value / 1000000, 1)  # Normalizacja do 1000000

    def _determine_risk_category(self, score: float) -> str:
        """Określenie kategorii ryzyka."""
        if score >= 0.8:
            return "Niskie ryzyko"
        elif score >= 0.6:
            return "Średnio-niskie ryzyko"
        elif score >= 0.4:
            return "Średnie ryzyko"
        elif score >= 0.2:
            return "Średnio-wysokie ryzyko"
        else:
            return "Wysokie ryzyko"

    def _generate_recommendations(self, risk_components: Dict[str, float]) -> List[str]:
        """Generowanie rekomendacji na podstawie oceny komponentów."""
        recommendations = []
        
        if risk_components['financial_stability'] < 0.4:
            recommendations.append("Zalecana poprawa stabilności finansowej")
            
        if risk_components['income_reliability'] < 0.4:
            recommendations.append("Wymagane dodatkowe potwierdzenie źródeł dochodu")
            
        if risk_components['employment_stability'] < 0.4:
            recommendations.append("Rozważ zabezpieczenie dodatkowe ze względu na niestabilność zatrudnienia")
            
        if risk_components['credit_history'] < 0.4:
            recommendations.append("Wymagane wyjaśnienie historii kredytowej")
            
        if risk_components['assets'] < 0.4:
            recommendations.append("Rozważ dodatkowe zabezpieczenie majątkowe")
            
        return recommendations

# Przykład użycia
if __name__ == "__main__":
    # Inicjalizacja agenta
    agent = DocumentRiskAgent()
    
    # Przykładowe dokumenty
    example_documents = {
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
    validated_docs = agent.validate_documents(example_documents)
    
    # Obliczenie ryzyka
    risk_assessment = agent.calculate_risk_score(validated_docs)
    
    print("Ocena ryzyka:", risk_assessment) 