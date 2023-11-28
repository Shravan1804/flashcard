import dash_bootstrap_components as dbc
import diskcache
from dash import Dash, DiskcacheManager
from dotenv import load_dotenv

from src.web_app.callbacks import register_callbacks
from src.web_app.layouts import get_app_layout

if __name__ == "__main__":
    load_dotenv()
    cache = diskcache.Cache("./cache")
    app = Dash(
        __name__,
        external_stylesheets=[dbc.themes.BOOTSTRAP],
        background_callback_manager=DiskcacheManager(cache),
        assets_folder="../assets",
    )
    app.layout = get_app_layout()
    register_callbacks()
    app.run(debug=True)
