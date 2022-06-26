from dash import html, dcc
import dash_bootstrap_components as dbc
from style_display.style import  homepage_icon_style, page_style




app_description = html.Div(
    style=page_style,
    children=[
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H3(
                            "Envio Client Portfolio analytics",
                            style={"color": "#FFFFFF"},
                        ),
                        html.Br(),
                        html.Br(),
                        dbc.Modal(
                            id="nodata_popup",
                            is_open=False,
                            children=[
                                dbc.ModalHeader(dbc.ModalTitle(id="site_name")),
                                dbc.ModalBody(id="desc_site_info"),
                            ],
                        ),
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
                                    src=ENVIO_ASSET_IMAGE,
                                    # top=True,
                                    style=homepage_icon_style,
                                ),
                                dbc.CardLink(
                                    children=[
                                        dbc.CardImgOverlay(
                                            [
                                                dbc.CardBody(
                                                    html.H3(
                                                        "Asset Portfolio",
                                                        style={"margin": "5%"},
                                                    )
                                                )
                                            ]
                                        )
                                    ],
                                    href="asset",
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
                                                        "Building Assets",
                                                        style={"margin": "5%"},
                                                    )
                                                )
                                            ]
                                        )
                                    ],
                                    href="site_asset",
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
                                                        "Building Weather data",
                                                        style={"margin": "5%"},
                                                    )
                                                )
                                            ]
                                        )
                                    ],
                                    href="site_weather",
                                ),
                            ],
                            style={"width": "18rem", "height": "18rem"},
                        )
                    ]
                ),
            ]
        ),
        html.Br(),
        dbc.Row(
                [
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
                                                            "CTI Analysis",
                                                            style={"margin": "5%"},
                                                        )
                                                    )
                                                ]
                                            )
                                        ],
                                        href="cti",
                                    ),
                                ],
                                style={"width": "18rem", "height": "18rem"},
                            )
                        ]
                    )
                ]
            ),
    ],
)




