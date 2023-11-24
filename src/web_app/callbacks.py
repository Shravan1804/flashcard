import time

import dash

from ..web_app.layouts import ContentIdentifiers, LayoutIdentifiers


def register_callbacks():
    @dash.callback(
        output=[
            dash.Output(LayoutIdentifiers.GENERATED_CONCEPTS.name, "options"),
            dash.Output(LayoutIdentifiers.GENERATED_CONCEPTS.name, "value"),
            dash.Output(LayoutIdentifiers.CONTAINER.name, "active_item"),
            dash.Output(LayoutIdentifiers.GENERATE_CONCEPTS_LOADING.name, "children"),
        ],
        inputs=dict(
            n_click=dash.Input(LayoutIdentifiers.GENERATE_CONCEPTS.name, "n_clicks"),
            language=dash.State(LayoutIdentifiers.LANGUAGE.name, "value"),
            prompt=dash.State(LayoutIdentifiers.PROMPT.name, "value"),
        ),
        running=[
            (
                dash.Output(LayoutIdentifiers.GENERATE_CONCEPTS.name, "disabled"),
                True,
                False,
            ),
        ],
        prevent_initial_call=True,
        background=True,
    )
    def on_generate_concepts(n_click, language, prompt):
        time.sleep(2)
        concepts = [f"concept{i}" for i in range(15)]  # TODO: generate concepts
        return concepts, concepts, ContentIdentifiers.CONCEPTS.name, ""
