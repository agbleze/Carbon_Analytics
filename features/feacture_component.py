from dash import html, dcc
import dash_bootstrap_components as dbc
from style_display.style import homepage_icon_style



def CardButton(cardimg_style: dict = homepage_icon_style,
               card_title: str = 'Card Title',
               cardlink_href="card_href"):
    return dbc.Col(
                        [
                            dbc.Card(
                                [
                                    dbc.CardImg(
                                        style=cardimg_style,
                                    ),
                                    dbc.CardLink(
                                        children=[
                                            dbc.CardImgOverlay(
                                                [
                                                    dbc.CardBody(
                                                        html.H3(
                                                            children=card_title,
                                                            style={"margin": "5%"},
                                                        )
                                                    )
                                                ]
                                            )
                                        ],
                                        href=cardlink_href,
                                    ),
                                ],
                                style={"width": "18rem", "height": "18rem"},
                            )
                        ]
                    )




