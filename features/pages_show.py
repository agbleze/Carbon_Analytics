#%%
import dash_trich_components as dtc
from dash import dcc
import dash_bootstrap_components as dbc
from dash import html

#%%
card_icon = {
    "color": "green",
    "textAlign": "center",
    "fontSize": "4em",
    "margin": "auto",
}

portfolio = html.Div(
    [
        dbc.Container(
            [
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                dbc.CardGroup(
                                    [
                                        dbc.Card(
                                            dbc.CardBody(
                                                [
                                                    html.H2(
                                                        id="total_client",
                                                        className="card-title",
                                                    ),
                                                    html.P(
                                                        "Total clients",
                                                        className="card-text",
                                                    ),
                                                ]
                                            )
                                        ),
                                        dbc.Card(
                                            html.Div(
                                                className="bi bi-people-fill",
                                                style=card_icon,
                                            ),
                                            style={
                                                "maxWidth": 195,
                                                "backgroundColor": "#e4ac23",
                                            },
                                        ),
                                    ]
                                )
                            ]
                        ),
                        ## Number of buildings
                        dbc.Col(
                            [
                                dbc.CardGroup(
                                    [
                                        dbc.Card(
                                            dbc.CardBody(
                                                [
                                                    html.H2(
                                                        id="total_building",
                                                        className="card-title",
                                                    ),
                                                    html.P(
                                                        "Total building",
                                                        className="card-text",
                                                    ),
                                                ]
                                            )
                                        ),
                                        dbc.Card(
                                            html.Div(
                                                className="bi bi-house-fill",
                                                style=card_icon,
                                            ),
                                            style={
                                                "maxWidth": 195,
                                                "backgroundColor": "#e4ac23",
                                            },
                                        ),
                                    ]
                                )
                            ]
                        ),
                        ## Total area of buildings
                        dbc.Col(
                            [
                                dbc.CardGroup(
                                    [
                                        dbc.Card(
                                            dbc.CardBody(
                                                [
                                                    html.H3(
                                                        id="total_building_area",
                                                        className="card-title",
                                                    ),
                                                    html.P(
                                                        "Total building Area (square meters)",
                                                        className="card-text",
                                                    ),
                                                ]
                                            )
                                        ),
                                        dbc.Card(
                                            html.Div(
                                                className="bi bi-building",
                                                style=card_icon,
                                            ),
                                            style={
                                                "maxWidth": 195,
                                                "backgroundColor": "#e4ac23",
                                            },
                                        ),
                                    ]
                                )
                            ]
                        ),
                    ]
                ),
                html.Br(), html.Br(),
                dbc.Row(
                    [
                        ## Average area of buildings
                        dbc.Col(
                            [
                                dbc.CardGroup(
                                    [
                                        dbc.Card(
                                            dbc.CardBody(
                                                [
                                                    html.H3(
                                                        id="average_building_area",
                                                        className="card-title",
                                                    ),
                                                    html.P(
                                                        "Average building Area (square meters)",
                                                        className="card-text",
                                                    ),
                                                ]
                                            )
                                        ),
                                        dbc.Card(
                                            html.Div(
                                                className="bi bi-bank2",
                                                style=card_icon,
                                            ),
                                            style={
                                                "maxWidth": 195,
                                                "backgroundColor": "#e4ac23",
                                            },
                                        ),
                                    ]
                                )
                            ]
                        ),
                        ## Number of countries
                        dbc.Col(
                            [
                                dbc.CardGroup(
                                    [
                                        dbc.Card(
                                            dbc.CardBody(
                                                [
                                                    html.H2(
                                                        id="total_countries",
                                                        className="card-title",
                                                    ),
                                                    html.P(
                                                        "Total countries operated in",
                                                        className="card-text",
                                                    ),
                                                ]
                                            )
                                        ),
                                        dbc.Card(
                                            html.Div(
                                                className="bi bi-geo-alt-fill",
                                                style=card_icon,
                                            ),
                                            style={
                                                "maxWidth": 195,
                                                "backgroundColor": "#e4ac23",
                                            },
                                        ),
                                    ]
                                )
                            ]
                        ),
                        ## Number of cities operated in
                        dbc.Col(
                            [
                                dbc.CardGroup(
                                    [
                                        dbc.Card(
                                            dbc.CardBody(
                                                [
                                                    html.H2(
                                                        id="total_cities",
                                                        className="card-title",
                                                    ),
                                                    html.P(
                                                        "Total number of cities operated in",
                                                        className="card-text",
                                                    ),
                                                ]
                                            )
                                        ),
                                        dbc.Card(
                                            html.Div(
                                                className="bi bi-geo-fill",
                                                style=card_icon,
                                            ),
                                            style={
                                                "maxWidth": 195,
                                                "backgroundColor": "#e4ac23",
                                            },
                                        ),
                                    ]
                                )
                            ]
                        ),
                    ]
                ),
            ]
        )
    ]
)


client_dashboard = html.Div(
    [
        dbc.Container(
            [
                dbc.Row(
                    [
                        dbc.Col(
                            id="client_dropdown", lg=2, style={"paddingLeft": "0%"}
                        ),
                        dbc.Col(
                            id="client_portfolio",
                            lg=10,
                            children=[
                                dbc.Row(
                                    [
                                        dbc.Col(
                                            dbc.CardGroup(
                                                [
                                                    dbc.Card(
                                                        dbc.CardBody(
                                                            [
                                                                html.H3(
                                                                    id="client_total_building",
                                                                    className="card-title",
                                                                ),
                                                                html.P(
                                                                    "Total building",
                                                                    className="card-text",
                                                                ),
                                                            ]
                                                        )
                                                    ),
                                                    dbc.Card(
                                                        html.Div(
                                                            className="bi bi-house-fill",
                                                            style=card_icon,
                                                        ),
                                                        style={
                                                            "maxWidth": 195,
                                                            "backgroundColor": "#e4ac23",
                                                        },
                                                    ),
                                                ]
                                            )
                                        ),
                                        dbc.Col(
                                            dbc.CardGroup(
                                                [
                                                    dbc.Card(
                                                        dbc.CardBody(
                                                            [
                                                                html.H3(
                                                                    id="client_total_building_area",
                                                                    className="card-title",
                                                                ),
                                                                html.P(
                                                                    "Total building Area (square meters)",
                                                                    className="card-text",
                                                                ),
                                                            ]
                                                        )
                                                    ),
                                                    dbc.Card(
                                                        html.Div(
                                                            className="bi bi-building",
                                                            style=card_icon,
                                                        ),
                                                        style={
                                                            "maxWidth": 195,
                                                            "backgroundColor": "#e4ac23",
                                                        },
                                                    ),
                                                ]
                                            )
                                        ),
                                        dbc.Col(
                                            dbc.CardGroup(
                                                [
                                                    dbc.Card(
                                                        dbc.CardBody(
                                                            [
                                                                html.H3(
                                                                    id="client_average_building_area",
                                                                    className="card-title",
                                                                ),
                                                                html.P(
                                                                    "Average building Area (square meters)",
                                                                    className="card-text",
                                                                ),
                                                            ]
                                                        )
                                                    ),
                                                    dbc.Card(
                                                        html.Div(
                                                            className="bi bi-box",
                                                            style=card_icon,
                                                        ),
                                                        style={
                                                            "maxWidth": 195,
                                                            "backgroundColor": "#e4ac23",
                                                        },
                                                    ),
                                                ]
                                            )
                                        ),
                                    ]
                                ),
                                html.Br(),
                                dbc.Row(
                                    [
                                        dbc.Col(
                                            dbc.CardGroup(
                                                [
                                                    dbc.Card(
                                                        dbc.CardBody(
                                                            [
                                                                html.H3(
                                                                    id="client_total_points",
                                                                    className="card-title",
                                                                ),
                                                                html.P(
                                                                    "Total Equipment Points",
                                                                    className="card-text",
                                                                ),
                                                            ]
                                                        )
                                                    ),
                                                    dbc.Card(
                                                        html.Div(
                                                            className="bi bi-file-easel-fill",
                                                            style=card_icon,
                                                        ),
                                                        style={
                                                            "maxWidth": 195,
                                                            "backgroundColor": "#e4ac23",
                                                        },
                                                    ),
                                                ]
                                            )
                                        ),
                                        dbc.Col(
                                            dbc.CardGroup(
                                                [
                                                    dbc.Card(
                                                        dbc.CardBody(
                                                            [
                                                                html.H3(
                                                                    id="client_total_equipment",
                                                                    className="card-title",
                                                                ),
                                                                html.P(
                                                                    "Total Equipment",
                                                                    className="card-text",
                                                                ),
                                                            ]
                                                        )
                                                    ),
                                                    dbc.Card(
                                                        html.Div(
                                                            className="bi bi-cpu-fill",
                                                            style=card_icon,
                                                        ),
                                                        style={
                                                            "maxWidth": 195,
                                                            "backgroundColor": "#e4ac23",
                                                        },
                                                    ),
                                                ]
                                            )
                                        ),
                                        dbc.Col(
                                            dbc.CardGroup(
                                                [
                                                    dbc.Card(
                                                        dbc.CardBody(
                                                            [
                                                                html.H3(
                                                                    id="client_total_rooms",
                                                                    className="card-title",
                                                                ),
                                                                html.P(
                                                                    "Total rooms",
                                                                    className="card-text",
                                                                ),
                                                            ]
                                                        )
                                                    ),
                                                    dbc.Card(
                                                        html.Div(
                                                            className="bi bi-door-closed",
                                                            style=card_icon,
                                                        ),
                                                        style={
                                                            "maxWidth": 195,
                                                            "backgroundColor": "#e4ac23",
                                                        },
                                                    ),
                                                ]
                                            )
                                        ),
                                    ]
                                ),
                            ],
                        ),
                    ]
                )
            ]
        ),
        html.Br(),
        html.Br(),
        html.Div(id="client_buildings_table"),
        html.Br(),
        html.Div(id="client_equipment_graph"),
    ]
)


content_3 = html.Div(
    [
        html.Br(),
        dbc.Row(
            [
                dbc.Col(
                    lg=4,
                    children=[
                        dbc.Label("Select Building size"),
                        dcc.RangeSlider(
                            min=0,
                            max=500_000,
                            value=(20_000, 100_000),
                            id="building_size",
                            tooltip={"placement": "bottom", "always_visible": True},
                            allowCross=False
                        ),
                    ],
                ),
                dbc.Col(
                    lg=8,
                    children=[
                        dbc.Row(
                            [
                                dbc.Col(
                                    dbc.CardGroup(
                                        [
                                            dbc.Card(
                                                dbc.CardBody(
                                                    [
                                                        html.H3(
                                                            id="bs_total_clients",
                                                            className="card-title",
                                                        ),
                                                        html.P(
                                                            "Total Clients",
                                                            className="card-text",
                                                        ),
                                                    ]
                                                )
                                            ),
                                            dbc.Card(
                                                html.Div(
                                                    className="bi bi-people-fill",
                                                    style=card_icon,
                                                ),
                                                style={
                                                    "maxWidth": 195,
                                                    "backgroundColor": "#e4ac23",
                                                },
                                            ),
                                        ]
                                    )
                                ),
                                dbc.Col(
                                    dbc.CardGroup(
                                        [
                                            dbc.Card(
                                                dbc.CardBody(
                                                    [
                                                        html.H3(
                                                            id="bs_total_buildings",
                                                            className="card-title",
                                                        ),
                                                        html.P(
                                                            "Total Buildings",
                                                            className="card-text",
                                                        ),
                                                    ]
                                                )
                                            ),
                                            dbc.Card(
                                                html.Div(
                                                    className="bi bi-house-fill",
                                                    style=card_icon,
                                                ),
                                                style={
                                                    "maxWidth": 195,
                                                    "backgroundColor": "#e4ac23",
                                                },
                                            ),
                                        ]
                                    )
                                ),
                                dbc.Col(
                                    dbc.CardGroup(
                                        [
                                            dbc.Card(
                                                dbc.CardBody(
                                                    [
                                                        html.H3(
                                                            id="bs_total_equipments",
                                                            className="card-title",
                                                        ),
                                                        html.P(
                                                            "Total Equipments",
                                                            className="card-text",
                                                        ),
                                                    ]
                                                )
                                            ),
                                            dbc.Card(
                                                html.Div(
                                                    className="bi bi-cpu-fill",
                                                    style=card_icon,
                                                ),
                                                style={
                                                    "maxWidth": 195,
                                                    "backgroundColor": "#e4ac23",
                                                },
                                            ),
                                        ]
                                    )
                                ),
                            ]
                        ),
                        html.Br(),
                        dbc.Row(
                            [
                                dbc.Col(
                                    dbc.CardGroup(
                                        [
                                            dbc.Card(
                                                dbc.CardBody(
                                                    [
                                                        html.H3(
                                                            id="bs_total_equipment_points",
                                                            className="card-title",
                                                        ),
                                                        html.P(
                                                            "Total Equipment Points",
                                                            className="card-text",
                                                        ),
                                                    ]
                                                )
                                            ),
                                            dbc.Card(
                                                html.Div(
                                                    className="bi bi-grid-3x3-gap",
                                                    style=card_icon,
                                                ),
                                                style={
                                                    "maxWidth": 195,
                                                    "backgroundColor": "#e4ac23",
                                                },
                                            ),
                                        ]
                                    )
                                )
                            ]
                        ),
                    ],
                ),
            ]
        ),
        html.Br(),
        html.Br(),
        dbc.Row(
            [html.Div(id="bs_client_building_table"), html.Div(id="bs_building_table")]
        ),
    ]
)

content_4 = html.Div(
    [
        html.Br(),
        dbc.Row(
            [
                dbc.Col(
                    lg=3,
                    children=[
                        dbc.Label(
                            "Select number of clusters for Kmeans\
                                           clustering",
                            style={"color": "black"},
                        ),
                        dcc.Slider(
                            min=0,
                            max=10,
                            step=1,
                            value=4,
                            id="num_clusters",
                            tooltip={"placement": "bottom", "always_visible": True},
                        ),
                    ],
                ),
                dbc.Col(
                    lg=9,
                    children=[
                        dcc.Markdown(
                            """

                                ### Client segmentation based on portfolio

                                This analysis aims to group clients into clusters
                                of similarity based on clients' portfolio size.
                                Portfolio size is one of the several indicators
                                use to measure
                                the importance or relevance of a client to our growth hence
                                its use for the analysis.

                                The practical utility of this analysis is not limited to the following:

                                1. Among others, there is the possibility of targeting clients and
                                offering them certain features based on portfolio size.

                                2. The analysis provides a clue to understanding what is at stack
                                when in business discussions with clients. For example, we do not want to loss
                                clients in a cluster of high portfolio and the approach to clients
                                in such group  may be critical compared to clients in a group of smaller
                                portfolio size. This could also lead to prioritizing pain points of
                                clients in a group of higher portfolio as dissatifaction means lossing
                                a client with sizable share of our portfolio.

                                Kmeans clustering analysis was undertaken based of the average number of
                                equipments, buildings, points, buildings area and number of rooms of clients.

                                The results indicates clients can be optimally grouped into 4 clusters.

                            """
                        )
                    ],
                    style={"fontSize": "1.3em", "color": "black"},
                ),
            ]
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(children=[dcc.Graph(id="cluster_graph")], lg=4),
                dbc.Col(id="cluster_table", lg=8),
            ]
        ),
        html.Br(),
        html.Br(),
        dbc.Row([dbc.Col(lg=8, children=[dcc.Graph(id="inertia_graph")])]),
    ]
)


content_5 = html.Div("")

device_gateway_dashboard = html.Div(
    [
        dbc.Container(
            [
                dbc.Row(
                    [
                        dbc.Col(
                            id="device_building_dropdown", lg=3, style={"paddingLeft": "0%"}
                        ),
                        dbc.Col(
                            id="building_gateway",
                            lg=9,
                            children=[
                                dbc.Row(
                                    [
                                        dbc.Col(
                                            dbc.CardGroup(
                                                [
                                                    dbc.Card(
                                                        dbc.CardBody(
                                                            [
                                                                html.H3(
                                                                    id="building_total_gateway",
                                                                    className="card-title",
                                                                ),
                                                                html.P(
                                                                    "Number of ENVIO Gateways",
                                                                    className="card-text",
                                                                ),
                                                            ]
                                                        )
                                                    ),
                                                    dbc.Card(
                                                        html.Div(
                                                            className="bi bi-house-fill",
                                                            style=card_icon,
                                                        ),
                                                        style={
                                                            "maxWidth": 195,
                                                            "backgroundColor": "#e4ac23",
                                                        },
                                                    ),
                                                ]
                                            )
                                        ),
                                        dbc.Col(
                                            dbc.CardGroup(
                                                [
                                                    dbc.Card(
                                                        dbc.CardBody(
                                                            [
                                                                html.H3(
                                                                    id="total_building_devices",
                                                                    className="card-title",
                                                                ),
                                                                html.P(
                                                                    "Total building Devices",
                                                                    className="card-text",
                                                                ),
                                                            ]
                                                        )
                                                    ),
                                                    dbc.Card(
                                                        html.Div(
                                                            className="bi bi-building",
                                                            style=card_icon,
                                                        ),
                                                        style={
                                                            "maxWidth": 195,
                                                            "backgroundColor": "#e4ac23",
                                                        },
                                                    ),
                                                ]
                                            )
                                        ),
                                        dbc.Col(
                                            dbc.CardGroup(
                                                [
                                                    dbc.Card(
                                                        dbc.CardBody(
                                                            [
                                                                html.H3(
                                                                    id="gateway_per_unit_area",
                                                                    className="card-title",
                                                                ),
                                                                html.P(
                                                                    "Gateway per Unit Area",
                                                                    className="card-text",
                                                                ),
                                                            ]
                                                        )
                                                    ),
                                                    dbc.Card(
                                                        html.Div(
                                                            className="bi bi-box",
                                                            style=card_icon,
                                                        ),
                                                        style={
                                                            "maxWidth": 195,
                                                            "backgroundColor": "#e4ac23",
                                                        },
                                                    ),
                                                ]
                                            )
                                        ),
                                    ]
                                ),
                                html.Br(),
                                dbc.Row(
                                    [
                                        dbc.Col(
                                            dbc.CardGroup(
                                                [
                                                    dbc.Card(
                                                        dbc.CardBody(
                                                            [
                                                                html.H3(
                                                                    id="device_per_unit_area",
                                                                    className="card-title",
                                                                ),
                                                                html.P(
                                                                    "Device per unit Area",
                                                                    className="card-text",
                                                                ),
                                                            ]
                                                        )
                                                    ),
                                                    dbc.Card(
                                                        html.Div(
                                                            className="bi bi-file-easel-fill",
                                                            style=card_icon,
                                                        ),
                                                        style={
                                                            "maxWidth": 195,
                                                            "backgroundColor": "#e4ac23",
                                                        },
                                                    ),
                                                ]
                                            )
                                        )
                                        # dbc.Col(
                                        #     dbc.CardGroup(
                                        #         [
                                        #             dbc.Card(
                                        #                 dbc.CardBody(
                                        #                     [
                                        #                         html.H3(
                                        #                             id="client_total_equipment",
                                        #                             className="card-title",
                                        #                         ),
                                        #                         html.P(
                                        #                             "Total Equipment",
                                        #                             className="card-text",
                                        #                         ),
                                        #                     ]
                                        #                 )
                                        #             ),
                                        #             dbc.Card(
                                        #                 html.Div(
                                        #                     className="bi bi-cpu-fill",
                                        #                     style=card_icon,
                                        #                 ),
                                        #                 style={
                                        #                     "maxWidth": 195,
                                        #                     "backgroundColor": "#e4ac23",
                                        #                 },
                                        #             ),
                                        #         ]
                                        #     )
                                        # ),
                                        # dbc.Col(
                                        #     dbc.CardGroup(
                                        #         [
                                        #             dbc.Card(
                                        #                 dbc.CardBody(
                                        #                     [
                                        #                         html.H3(
                                        #                             id="client_total_rooms",
                                        #                             className="card-title",
                                        #                         ),
                                        #                         html.P(
                                        #                             "Total rooms",
                                        #                             className="card-text",
                                        #                         ),
                                        #                     ]
                                        #                 )
                                        #             ),
                                        #             dbc.Card(
                                        #                 html.Div(
                                        #                     className="bi bi-door-closed",
                                        #                     style=card_icon,
                                        #                 ),
                                        #                 style={
                                        #                     "maxWidth": 195,
                                        #                     "backgroundColor": "#e4ac23",
                                        #                 },
                                        #             ),
                                        #         ]
                                        #     )
                                        # ),
                                    ]
                                ),
                            ],
                        ),
                    ]
                )
            ]
        ),
        html.Br(),
        html.Br(),
        dbc.Row([dbc.Col(id='col_gateway_table',
                         children=[
                                    html.H5('Gateways'),
                                    html.Div(id="gateway_table")
                                   ]
                         ), 
                 dbc.Col(id='col_device_table',
                         children=[
                                    html.H5('Devices'),
                                    html.Div(id='device_table')
                                   ]
                         )
                 ]
                ),        
        html.Br(),
        # dbc.Row(
        #     [
        #         dbc.Col(
        #             [
        #                 dcc.Loading(
        #                     id="loading_cach_device_gateway_data_stored",
        #                     type="cube",
        #                     fullscreen=True,
        #                     children=[dcc.Store(id="cach_device_gateway_data_stored")
        #                               ]
        #                 ),
        #             ]
        #         )
        #     ]
        # )
    ]
)

layout = html.Div(
    [
        dtc.SideBar(
            [
                dtc.SideBarItem(
                    id="id_1",
                    label="Portfolio summary",
                    icon="fas fa-infinity"
                ),
                dtc.SideBarItem(
                    id="id_2", label="Client portfolio", icon="fa fa-user-circle"
                ),
                dtc.SideBarItem(
                    id="id_3",
                    label="Building size",
                    icon="fas fa-hotel"
                ),
                dtc.SideBarItem(
                    id="id_4", label="Customer segmentation", icon="fas fa-chart-line"
                ),
                dtc.SideBarItem(
                    id='device_gateway',
                    label="Devices and Gateways",
                    icon='bi bi-diagram-3-fill'
                ),
                dtc.SideBarItem(id="id_5", label="Metrics", icon="fas fa-cog"),
            ]
        ),
        html.Div([], id="page_content"),
    ]
)
