from dash import html, dcc
import dash_bootstrap_components as dbc
from StyleDisplay.style import homepage_icon_style



def CardButton(cardimg_src: str = None, 
               cardimg_style: dict = homepage_icon_style,
               id_card_body: str = 'id_card',
               card_title: str =  None,#'Card Title',
               cardlink_href: str = "card_href",
               headstyle: dict = {"margin": "5%"},
               card_style: dict = {"width": "18rem", "height": "18rem"}
               ):
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
                                                        html.H1(id=id_card_body,
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




