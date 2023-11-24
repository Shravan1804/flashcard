from dash import Input, Output, State, callback

from ..web_app.layouts import LayoutIdentifiers, PageIdentifiers


def register_callbacks():
    @callback(
        output={p.name: Output(p.name, "style") for p in PageIdentifiers},
        inputs={"pathname": Input("url", "pathname")},
    )
    def render_page_content(pathname):
        ret = {p.name: {"display": "none"} for p in PageIdentifiers}
        for p in PageIdentifiers:
            if pathname == "/":
                ret[PageIdentifiers.HOME.name] = {"display": "block"}
            elif pathname == f"/{p.name.lower()}":
                ret[p.name] = {"display": "block"}
        return ret

    @callback(
        output=[
            Output(LayoutIdentifiers.GENERATED_CONCEPTS.name, "options"),
            Output(LayoutIdentifiers.GENERATED_CONCEPTS.name, "value"),
            Output("url", "pathname"),
        ],
        inputs=dict(
            n_clicks=Input(LayoutIdentifiers.GENERATE_CONCEPTS.name, "n_clicks"),
            language=State(LayoutIdentifiers.LANGUAGE.name, "value"),
            prompt=State(LayoutIdentifiers.PROMPT.name, "value"),
        ),
        prevent_initial_call=True,
    )
    def render_concepts(n_clicks, language, prompt):
        concepts = ["concept1", "concept2", "concept3"]  # TODO: generate concepts
        return concepts, concepts, f"/{PageIdentifiers.CONCEPTS.name.lower()}"
