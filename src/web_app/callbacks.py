import time

import dash

from ..web_app.layouts import (
    ContentBlockIdentifier,
    LayoutIdentifiers,
    get_flashcards_layout,
)


def register_callbacks():
    @dash.callback(
        output=dict(
            new_concept_options=dash.Output(
                LayoutIdentifiers.GENERATED_CONCEPTS.name, "options"
            ),
            new_concepts=dash.Output(
                LayoutIdentifiers.GENERATED_CONCEPTS.name, "value"
            ),
            next_block=dash.Output(
                LayoutIdentifiers.CONTENT_CONTAINER.name, "active_item"
            ),
            loading_item=dash.Output(
                LayoutIdentifiers.GENERATE_CONCEPTS_LOADING.name, "children"
            ),
        ),
        inputs=dict(
            n_click=dash.Input(LayoutIdentifiers.GENERATE_CONCEPTS.name, "n_clicks"),
            language=dash.State(LayoutIdentifiers.LANGUAGE.name, "value"),
            prompt=dash.State(LayoutIdentifiers.PROMPT.name, "value"),
            already_generated_concepts=dash.State(
                LayoutIdentifiers.GENERATED_CONCEPTS.name, "options"
            ),
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
    def on_generate_concepts(n_click, language, prompt, already_generated_concepts):
        time.sleep(2)
        new_concepts = [f"concept{i:03}" for i in range(15)]  # TODO: generate concepts
        new_concepts = sorted(
            [c for c in new_concepts if c not in already_generated_concepts]
        )
        new_concept_options = sorted(already_generated_concepts + new_concepts)
        return dict(
            new_concept_options=new_concept_options,
            new_concepts=new_concepts,
            next_block=ContentBlockIdentifier.CONCEPTS.name,
            loading_item="",
        )

    @dash.callback(
        output=dict(
            patched_flashcards=dash.Output(
                LayoutIdentifiers.GENERATED_FLASHCARDS.name, "children"
            ),
            next_block=dash.Output(
                LayoutIdentifiers.CONTENT_CONTAINER.name,
                "active_item",
                allow_duplicate=True,
            ),
            loading_item=dash.Output(
                LayoutIdentifiers.GENERATE_FLASHCARDS_LOADING.name, "children"
            ),
        ),
        inputs=dict(
            n_click=dash.Input(LayoutIdentifiers.GENERATE_FLASHCARDS.name, "n_clicks"),
            language=dash.State(LayoutIdentifiers.LANGUAGE.name, "value"),
            prompt=dash.State(LayoutIdentifiers.PROMPT.name, "value"),
            new_concepts=dash.State(LayoutIdentifiers.GENERATED_CONCEPTS.name, "value"),
        ),
        running=[
            (
                dash.Output(LayoutIdentifiers.GENERATE_FLASHCARDS.name, "disabled"),
                True,
                False,
            ),
        ],
        prevent_initial_call=True,
        background=True,
    )
    def on_generate_flashcards(n_click, language, prompt, new_concepts):
        time.sleep(2)
        # TODO: generate flashcards
        new_flashcard_rows = get_flashcards_layout(new_concepts)
        patched_flashcards = dash.Patch()
        for new_flashcard_row in reversed(new_flashcard_rows):
            patched_flashcards.prepend(new_flashcard_row)
        return dict(
            patched_flashcards=patched_flashcards,
            next_block=ContentBlockIdentifier.FLASHCARDS.name,
            loading_item="",
        )
