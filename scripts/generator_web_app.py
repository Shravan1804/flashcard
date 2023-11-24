import dash_bootstrap_components as dbc
import diskcache
from dash import Dash, DiskcacheManager

from src.web_app.callbacks import register_callbacks
from src.web_app.layouts import get_app_layout

if __name__ == "__main__":
    cache = diskcache.Cache("./cache")
    app = Dash(
        __name__,
        external_stylesheets=[dbc.themes.BOOTSTRAP],
        background_callback_manager=DiskcacheManager(cache),
    )
    app.layout = get_app_layout()
    register_callbacks()
    app.run(debug=True)
