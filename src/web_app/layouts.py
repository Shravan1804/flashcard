from enum import Enum

import dash_bootstrap_components as dbc
from babelnet.language import Language
from dash import dcc, html


class ContentBlockIdentifier(Enum):
    HOME = "Home"
    CONCEPTS = "Concepts"
    FLASHCARDS = "Flashcards"


class LayoutIdentifiers(Enum):
    CONTENT_CONTAINER = "CONTENT_CONTAINER"
    LANG = "LANG"
    DESCRIPTION = "DESCRIPTION"
    GENERATE_CONCEPTS = "GENERATE_CONCEPTS"
    GENERATE_CONCEPTS_LOADING = "GENERATE_CONCEPTS_LOADING"
    GENERATED_CONCEPTS = "GENERATED_CONCEPTS"
    GENERATE_FLASHCARDS = "GENERATE_FLASHCARDS"
    GENERATE_FLASHCARDS_LOADING = "GENERATE_FLASHCARDS_LOADING"
    GENERATED_FLASHCARDS = "GENERATED_FLASHCARDS"


def get_home_block():
    return dbc.Form(
        [
            dbc.Row(
                [
                    dbc.Label(
                        "Language", html_for=LayoutIdentifiers.LANG.name, width=2
                    ),
                    dbc.Col(
                        dcc.Dropdown(
                            id=LayoutIdentifiers.LANG.name,
                            options=sorted(
                                [
                                    Language(lang).value
                                    for lang in [
                                        "English",
                                        "Spanish",
                                        "French",
                                        "German",
                                        "Italian",
                                        "Portuguese",
                                        "Dutch",
                                        "Russian",
                                        "Chinese",
                                        "Korean",
                                    ]
                                ]
                            ),
                            value=Language.EN.value,
                        )
                    ),
                ],
                className="mb-3",
            ),
            dbc.Row(
                [
                    dbc.Label(
                        "Description",
                        html_for=LayoutIdentifiers.DESCRIPTION.name,
                        width=2,
                    ),
                    dbc.Col(
                        dbc.FormFloating(
                            [
                                dbc.Textarea(id=LayoutIdentifiers.DESCRIPTION.name),
                                dbc.Label("Concepts description (optional)"),
                            ]
                        )
                    ),
                ],
                className="mb-3",
            ),
            dbc.Button(
                "Generate concepts",
                id=LayoutIdentifiers.GENERATE_CONCEPTS.name,
                color="primary",
            ),
            dcc.Loading(
                type="default",
                children=html.Div(id=LayoutIdentifiers.GENERATE_CONCEPTS_LOADING.name),
            ),
        ]
    )


def get_concepts_block():
    return dbc.Form(
        [
            dbc.Row(
                [
                    dbc.Label(
                        "Generated concepts",
                        html_for=LayoutIdentifiers.GENERATED_CONCEPTS.name,
                        width=2,
                    ),
                    dbc.Col(
                        dcc.Dropdown(
                            [],
                            [],
                            multi=True,
                            id=LayoutIdentifiers.GENERATED_CONCEPTS.name,
                        ),
                    ),
                ],
                className="mb-3",
            ),
            dbc.Button(
                "Generate flashcards",
                id=LayoutIdentifiers.GENERATE_FLASHCARDS.name,
                color="primary",
            ),
            dcc.Loading(
                type="default",
                children=html.Div(
                    id=LayoutIdentifiers.GENERATE_FLASHCARDS_LOADING.name
                ),
            ),
        ],
    )


def get_flashcards_block():
    return html.Div(
        [],
        id=LayoutIdentifiers.GENERATED_FLASHCARDS.name,
    )


def create_flashcard_from_concept(flashcard_data):
    concept, definition, example, image = flashcard_data
    image = image if image else "assets/placeholder286x180.png"
    return dbc.Card(
        [
            dbc.CardImg(src=image, top=True),
            dbc.CardBody(
                [
                    html.H4(concept, className="card-title"),
                    html.P(
                        definition,
                        className="card-text",
                    ),
                    html.P(
                        example,
                        className="card-text",
                    ),
                ]
            ),
        ],
    )


def get_flashcards_layout(flashcards_data, ncols=5):
    flashcards = [
        create_flashcard_from_concept(flashcard_data)
        for flashcard_data in flashcards_data
    ]
    return [
        dbc.Row(
            [dbc.Col(fc) for fc in flashcards[i : i + ncols]],
            className="mb-4",
        )
        for i in range(0, len(flashcards), ncols)
    ]


def get_app_layout():
    return dbc.Container(
        [
            html.H1("Vocabulary Flashcard Generator"),
            html.Hr(),
            dbc.Accordion(
                [
                    dbc.AccordionItem(
                        get_home_block(),
                        title="Concept generation",
                        item_id=ContentBlockIdentifier.HOME.name,
                    ),
                    dbc.AccordionItem(
                        get_concepts_block(),
                        title="Flashcard generation",
                        item_id=ContentBlockIdentifier.CONCEPTS.name,
                    ),
                    dbc.AccordionItem(
                        get_flashcards_block(),
                        title="Generated flashcards",
                        item_id=ContentBlockIdentifier.FLASHCARDS.name,
                    ),
                ],
                id=LayoutIdentifiers.CONTENT_CONTAINER.name,
                active_item=ContentBlockIdentifier.HOME.name,
            ),
        ]
    )
