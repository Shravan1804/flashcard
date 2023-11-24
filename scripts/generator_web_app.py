import dash_bootstrap_components as dbc
from dash import Dash

from src.web_app.callbacks import register_callbacks
from src.web_app.layouts import get_layout

if __name__ == "__main__":
    app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
    app.layout = get_layout()
    register_callbacks()
    app.run(debug=True)
