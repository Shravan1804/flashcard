from enum import Enum

import dash_bootstrap_components as dbc
from dash import dcc, html


class PageIdentifiers(Enum):
    HOME = "Home"
    CONCEPTS = "Concepts"
    FLASHCARDS = "Flashcards"
    NOT_FOUND = "404: Not found"


class LayoutIdentifiers(Enum):
    LANGUAGE = "LANGUAGE"
    PROMPT = "PROMPT"
    GENERATE_CONCEPTS = "GENERATE_CONCEPTS"
    GENERATED_CONCEPTS = "GENERATED_CONCEPTS"
    GENERATE_FLASHCARDS = "GENERATE_FLASHCARDS"


def get_404_page():
    return html.Div(
        [
            html.H1(PageIdentifiers.NOT_FOUND.value, className="text-danger"),
            html.Hr(),
            html.P("The pathname was not recognised..."),
        ],
        className="p-3 bg-light rounded-3",
        id=PageIdentifiers.NOT_FOUND.name,
        style={"display": "none"},
    )


def get_home_page():
    return html.Div(
        [
            html.H3("Generate concepts"),
            dbc.Card(
                [
                    html.Div(
                        [
                            dbc.Label("Select language"),
                            dcc.Dropdown(
                                id=LayoutIdentifiers.LANGUAGE.name,
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
                                id=LayoutIdentifiers.PROMPT.name,
                                style={"width": "100%"},
                            ),
                        ]
                    ),
                    html.Div(
                        [
                            html.Button(
                                id=LayoutIdentifiers.GENERATE_CONCEPTS.name,
                                n_clicks=0,
                                children="Generate concepts",
                            )
                        ]
                    ),
                ],
                body=True,
            ),
        ],
        id=PageIdentifiers.HOME.name,
        style={"display": "none"},
    )


def get_concepts_page():
    return html.Div(
        [
            html.H3("Generated concepts"),
            dbc.Card(
                [
                    html.Div(
                        [
                            dbc.Label("Generated concepts"),
                            dcc.Dropdown(
                                [],
                                [],
                                multi=True,
                                id=LayoutIdentifiers.GENERATED_CONCEPTS.name,
                            ),
                        ]
                    ),
                    html.Div(
                        [
                            html.Button(
                                id=LayoutIdentifiers.GENERATE_FLASHCARDS.name,
                                n_clicks=0,
                                children="Generate flashcards",
                            )
                        ]
                    ),
                ],
                body=True,
            ),
        ],
        id=PageIdentifiers.CONCEPTS.name,
        style={"display": "none"},
    )


def get_flashcards_page():
    return html.Div(
        [
            html.H3("Generated flashcards"),
        ],
        id=PageIdentifiers.FLASHCARDS.name,
        style={"display": "none"},
    )


def get_app_layout():
    sidebar = html.Div(
        [
            html.H2("Flashcard Generator", className="display-4"),
            html.Hr(),
            dbc.Nav(
                [
                    dbc.NavLink(
                        p.value,
                        href="/" if p == PageIdentifiers.HOME else f"/{p.name.lower()}",
                        active="exact",
                    )
                    for p in PageIdentifiers
                    if p != PageIdentifiers.NOT_FOUND
                ],
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
            get_home_page(),
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
    return html.Div([dcc.Location(id="url", refresh="callback-nav"), sidebar, content])
