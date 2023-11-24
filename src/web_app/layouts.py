from enum import Enum

import dash_bootstrap_components as dbc
from dash import dcc, html


class Language(Enum):
    ENGLISH = "English"
    FRENCH = "French"
    GERMAN = "German"


class ContentBlockIdentifier(Enum):
    HOME = "Home"
    CONCEPTS = "Concepts"
    FLASHCARDS = "Flashcards"


class LayoutIdentifiers(Enum):
    CONTENT_CONTAINER = "CONTENT_CONTAINER"
    LANGUAGE = "LANGUAGE"
    PROMPT = "PROMPT"
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
                        "Language", html_for=LayoutIdentifiers.LANGUAGE.name, width=2
                    ),
                    dbc.Col(
                        dcc.Dropdown(
                            id=LayoutIdentifiers.LANGUAGE.name,
                            options=[lang.value for lang in Language],
                            value=Language.ENGLISH.value,
                        )
                    ),
                ],
                className="mb-3",
            ),
            dbc.Row(
                [
                    dbc.Label(
                        "Prompt", html_for=LayoutIdentifiers.PROMPT.name, width=2
                    ),
                    dbc.Col(
                        dbc.FormFloating(
                            [
                                dbc.Textarea(id=LayoutIdentifiers.PROMPT.name),
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
    return dbc.CardGroup(
        [],
        id=LayoutIdentifiers.GENERATED_FLASHCARDS.name,
    )


def get_flashcard(concept):
    return dbc.Card(
        [
            dbc.CardImg(src="/assets/placeholder286x180.png", top=True),
            dbc.CardBody(
                [
                    html.H4(concept, className="card-title"),
                    html.P(
                        "Definition",
                        className="card-text",
                    ),
                    html.P(
                        "Examples",
                        className="card-text",
                    ),
                ]
            ),
        ],
    )


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
