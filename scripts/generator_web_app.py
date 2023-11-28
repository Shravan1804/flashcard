import dash_bootstrap_components as dbc
import diskcache
from dash import Dash, DiskcacheManager
from dotenv import load_dotenv

load_dotenv()

from src.crawler.babelnet_crawler import BabelNetCrawler  # noqa: E402
from src.generator.concept_generator import ConceptGenerator  # noqa: E402
from src.web_app.callbacks import register_callbacks  # noqa: E402
from src.web_app.layouts import get_app_layout  # noqa: E402

if __name__ == "__main__":
    cache = diskcache.Cache("./cache")
    app = Dash(
        __name__,
        external_stylesheets=[dbc.themes.BOOTSTRAP],
        background_callback_manager=DiskcacheManager(cache),
        assets_folder="../assets",
    )
    app.layout = get_app_layout()
    concept_generator = ConceptGenerator(10)
    babelnet_crawler = BabelNetCrawler()
    register_callbacks(concept_generator, babelnet_crawler)
    app.run(debug=True)
