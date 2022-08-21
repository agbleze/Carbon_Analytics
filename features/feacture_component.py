from dash import html, dcc
import dash_bootstrap_components as dbc
from StyleDisplay.style import homepage_icon_style



def CardButton(cardimg_src: str = None, cardimg_style: dict = homepage_icon_style,
               card_title: str = 'Card Title',
               cardlink_href: str = "card_href",
               headstyle: dict = {"margin": "5%"},
               card_style: dict = {"width": "18rem", "height": "18rem"}):
    return dbc.Col(
                        [
                            dbc.Card(
                                [
                                    dbc.CardImg(
                                        src = cardimg_src,
                                        style=cardimg_style,
                                    ),
                                    dbc.CardLink(
                                        children=[
                                            dbc.CardImgOverlay(
                                                [
                                                    dbc.CardBody(
                                                        html.H3(
                                                            children=card_title,
                                                            style=headstyle,
                                                        )
                                                    )
                                                ]
                                            )
                                        ],
                                        href=cardlink_href,
                                    ),
                                ],
                                style= card_style,
                            )
                        ]
                    )




