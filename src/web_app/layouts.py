from enum import Enum

import dash_bootstrap_components as dbc
from dash import dcc, html


class PageIdentifiers(Enum):
    CONCEPTS = "CONCEPTS"
    FLASHCARDS = "FLASHCARDS"
    NOT_FOUND = "NOT_FOUND"


class LayoutIdentifiers(Enum):
    NAV = "NAV"
    LANGUAGE = "LANGUAGE"
    PROMPT = "PROMPT"
    GENERATE_CONCEPTS = "GENERATE_CONCEPTS"
    GENERATED_CONCEPTS = "GENERATED_CONCEPTS"
    GENERATE_FLASHCARDS = "GENERATE_FLASHCARDS"


def get_404_page():
    return html.Div(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P("The pathname was not recognised..."),
        ],
        className="p-3 bg-light rounded-3",
        id=PageIdentifiers.NOT_FOUND.value,
        style={"display": "none"},
    )


def get_concepts_layout(concepts):
    concepts = sorted(concepts)
    return [
        html.Div(
            [
                dbc.Label("Generated concepts"),
                dcc.Dropdown(concepts, concepts, multi=True),
            ]
        ),
        html.Div(
            [
                html.Button(
                    id=LayoutIdentifiers.GENERATE_FLASHCARDS.value,
                    n_clicks=0,
                    children="Generate flashcards",
                )
            ]
        ),
    ]


def get_concepts_page():
    content = [
        html.H3("Generate concepts"),
        dbc.Card(
            [
                html.Div(
                    [
                        dbc.Label("Select language"),
                        dcc.Dropdown(
                            id=LayoutIdentifiers.LANGUAGE.value,
                            options=["French", "English", "German"],
                            value="English",
                        ),
                    ]
                ),
                html.Div(
                    [
                        dbc.Label("Prompt"),
                        dcc.Textarea(
                            value="",
                            id=LayoutIdentifiers.PROMPT.value,
                            style={"width": "100%"},
                        ),
                    ]
                ),
                html.Div(
                    [
                        html.Button(
                            id=LayoutIdentifiers.GENERATE_CONCEPTS.value,
                            n_clicks=0,
                            children="Generate concepts",
                        )
                    ]
                ),
            ],
            body=True,
        ),
        dbc.Card(
            get_concepts_layout([]),
            id=LayoutIdentifiers.GENERATED_CONCEPTS.value,
            body=True,
            style={"display": "none"},
        ),
    ]
    return html.Div(
        content,
        id=PageIdentifiers.CONCEPTS.value,
        style={"display": "none"},
    )


def get_flashcards_page():
    return html.Div(
        [html.H3("Flashcards")],
        id=PageIdentifiers.FLASHCARDS.value,
        style={"display": "none"},
    )


def get_layout():
    sidebar = html.Div(
        [
            html.H2("Flashcard Generator", className="display-4"),
            html.Hr(),
            dbc.Nav(
                [
                    dbc.NavLink(
                        PageIdentifiers.CONCEPTS.value.lower().capitalize(),
                        href="/",
                        active="exact",
                    ),
                    dbc.NavLink(
                        PageIdentifiers.FLASHCARDS.value.lower().capitalize(),
                        href=f"/{PageIdentifiers.FLASHCARDS.value.lower()}",
                        active="exact",
                    ),
                ],
                id=LayoutIdentifiers.NAV.value,
                vertical=True,
                pills=True,
            ),
        ],
        style={
            "position": "fixed",
            "top": 0,
            "left": 0,
            "bottom": 0,
            "width": "18rem",
            "padding": "2rem 1rem",
            "background-color": "#f8f9fa",
        },
    )
    content = html.Div(
        [
            get_concepts_page(),
            get_flashcards_page(),
            get_404_page(),
        ],
        id="page-content",
        style={
            "margin-left": "18rem",
            "margin-right": "2rem",
            "padding": "2rem 1rem",
        },
    )
    return html.Div([dcc.Location(id="url"), sidebar, content])
