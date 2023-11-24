from dash import Input, Output, callback

from ..web_app.layouts import PageIdentifiers


def register_callbacks():
    @callback(
        output={p.value: Output(p.value, "style") for p in PageIdentifiers},
        inputs={"pathname": Input("url", "pathname")},
    )
    def render_page_content(pathname):
        ret = {p.value: {"display": "none"} for p in PageIdentifiers}
        for p in PageIdentifiers:
            if pathname == "/":
                ret[PageIdentifiers.CONCEPTS.value] = {"display": "block"}
            elif pathname == f"/{p.value.lower()}":
                ret[p.value] = {"display": "block"}
        return ret
