from dash import html, dcc
import dash_bootstrap_components as dbc
from StyleDisplay.style import  homepage_icon_style, page_style



def create_page_with_card_button(#self,
                                 title: str = 'Climate Analytics',
                                 card1_title:str = 'Carbon Emission Estimate',
                                 card2_title: str = 'Carbon Emission Prediction',
                                 card3_title: str = 'Statistical Analysis and \
                                                     Hypothesis Testing'):
 
    return dbc.Container(
        style=page_style,
        children=[
            dbc.Row(
                [
                    dbc.Col(
                        [
                            html.H3(
                                children=title,
                                style={"color": "#FFFFFF"},
                            ),
                            html.Br(),
                            html.Br(),
                        ]
                    )
                ]
            ),
            dbc.Row(
                [
                    dbc.Col(
                        [
                            dbc.Card(
                                [
                                    dbc.CardImg(
                                        #src=ENVIO_ASSET_IMAGE,
                                        # top=True,
                                        style=homepage_icon_style,
                                    ),
                                    dbc.CardLink(
                                        children=[
                                            dbc.CardImgOverlay(
                                                [
                                                    dbc.CardBody(
                                                        html.H3(
                                                            children = card1_title,
                                                            style={"margin": "5%"},
                                                        )
                                                    )
                                                ]
                                            )
                                        ],
                                        href="carbon_analytics",
                                    ),
                                ],
                                style={"width": "18rem", "height": "18rem"},
                            )
                        ]
                    ),
                    dbc.Col(
                        [
                            dbc.Card(
                                [
                                    dbc.CardImg(
                                        style=homepage_icon_style,
                                    ),
                                    dbc.CardLink(
                                        children=[
                                            dbc.CardImgOverlay(
                                                [
                                                    dbc.CardBody(
                                                        html.H3(
                                                            children=card2_title,
                                                            style={"margin": "5%"},
                                                        )
                                                    )
                                                ]
                                            )
                                        ],
                                        href="emission_prediction",
                                    ),
                                ],
                                style={"width": "18rem", "height": "18rem"},
                            )
                        ]
                    ),
                    dbc.Col(
                        [
                            dbc.Card(
                                [
                                    dbc.CardImg(
                                        style=homepage_icon_style,
                                    ),
                                    dbc.CardLink(
                                        children=[
                                            dbc.CardImgOverlay(
                                                [
                                                    dbc.CardBody(
                                                        html.H3(
                                                            children=card3_title,
                                                            style={"margin": "5%"},
                                                        )
                                                    )
                                                ]
                                            )
                                        ],
                                        href="hypothesis",
                                    ),
                                ],
                                style={"width": "18rem", "height": "18rem"},
                            )
                        ]
                    ),
                ]
            ),
            html.Br(),

        ],
    )
 #   return app_description




