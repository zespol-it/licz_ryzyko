import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np

class RiskDashboard:
    def __init__(self):
        self.app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
        self.setup_layout()
        self.setup_callbacks()

    def setup_layout(self):
        """Konfiguracja układu dashboardu."""
        self.app.layout = dbc.Container([
            dbc.Row([
                dbc.Col(html.H1("Dashboard Analizy Ryzyka", className="text-center mb-4"), width=12)
            ]),

            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardHeader("Wskaźniki Portfela"),
                        dbc.CardBody([
                            html.Div(id="portfolio-metrics")
                        ])
                    ])
                ], width=12, lg=6),

                dbc.Col([
                    dbc.Card([
                        dbc.CardHeader("Rozkład Ryzyka"),
                        dbc.CardBody([
                            dcc.Graph(id="risk-distribution")
                        ])
                    ])
                ], width=12, lg=6)
            ], className="mb-4"),

            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardHeader("Trend Spłat"),
                        dbc.CardBody([
                            dcc.Graph(id="repayment-trend")
                        ])
                    ])
                ], width=12)
            ], className="mb-4"),

            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardHeader("Analiza Windykacji"),
                        dbc.CardBody([
                            dcc.Graph(id="recovery-analysis")
                        ])
                    ])
                ], width=12, lg=6),

                dbc.Col([
                    dbc.Card([
                        dbc.CardHeader("Prognoza Odzysków"),
                        dbc.CardBody([
                            dcc.Graph(id="recovery-forecast")
                        ])
                    ])
                ], width=12, lg=6)
            ])
        ], fluid=True)

    def setup_callbacks(self):
        """Konfiguracja callbacków dla interaktywnych elementów."""
        
        @self.app.callback(
            Output("portfolio-metrics", "children"),
            Input("portfolio-data-store", "data")
        )
        def update_metrics(data):
            # Przykładowe dane
            metrics = {
                "Całkowita wartość portfela": "1,000,000 PLN",
                "Średni score ryzyka": "0.45",
                "Wskaźnik odzysku": "35%",
                "Aktywne sprawy": "1,250"
            }
            
            return [
                html.Div([
                    html.H5(key),
                    html.H3(value)
                ], className="text-center mb-3")
                for key, value in metrics.items()
            ]

        @self.app.callback(
            Output("risk-distribution", "figure"),
            Input("portfolio-data-store", "data")
        )
        def update_risk_distribution(data):
            # Przykładowe dane
            categories = ["Niskie", "Średnio-niskie", "Średnie", "Średnio-wysokie", "Wysokie"]
            values = [20, 35, 25, 15, 5]
            
            fig = go.Figure(data=[
                go.Bar(x=categories, y=values, marker_color='rgb(55, 83, 109)')
            ])
            
            fig.update_layout(
                title="Rozkład Kategorii Ryzyka",
                xaxis_title="Kategoria Ryzyka",
                yaxis_title="Liczba Przypadków",
                showlegend=False
            )
            
            return fig

        @self.app.callback(
            Output("repayment-trend", "figure"),
            Input("portfolio-data-store", "data")
        )
        def update_repayment_trend(data):
            # Przykładowe dane
            dates = pd.date_range(start='2023-01-01', periods=12, freq='M')
            values = np.cumsum(np.random.normal(1000, 100, 12))
            
            fig = px.line(
                x=dates, 
                y=values,
                title="Trend Spłat w Czasie"
            )
            
            fig.update_layout(
                xaxis_title="Data",
                yaxis_title="Wartość Spłat (PLN)"
            )
            
            return fig

    def run_server(self, debug=True, port=8050):
        """Uruchomienie serwera dashboardu."""
        self.app.run_server(debug=debug, port=port)

if __name__ == '__main__':
    dashboard = RiskDashboard()
    dashboard.run_server() 