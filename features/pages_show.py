#%%
import dash_trich_components as dtc
from dash import dcc
import dash_bootstrap_components as dbc
from dash import html
from helper_components import output_card

#%%
card_icon = {
    "color": "green",
    "textAlign": "center",
    "fontSize": "4em",
    "margin": "auto",
}

cardstyling = {"maxWidth": 195,
                    "backgroundColor": "#e4ac23",
                }
output_card(id = "total_client", 
            card_label="Total clients", 
            icon="bi bi-people-fill",
            style=cardstyling
            )
portfolio = html.Div(
    [
        dbc.Container(
            [
                dbc.Row(
                    [
                        output_card(id = "total_client", 
                                    card_label="Total clients", 
                                    icon="bi bi-people-fill",
                                    style=cardstyling
                                    ),
                        output_card(id = "total_building", 
                                    card_label="Total building", 
                                    icon="bi bi-house-fill",
                                    style=cardstyling
                                    ),
                        output_card(id = "total_building_area", 
                                    card_label="Total building Area (square meters)", 
                                    icon="bi bi-building",
                                    style=cardstyling
                                    )                        
                    ]
                ),
                html.Br(), html.Br(),
                dbc.Row(
                    [
                        output_card(id = "average_building_area", 
                                    card_label="Average building Area (square meters)", 
                                    icon="bi bi-bank2",
                                    style=cardstyling
                                    ),
                        output_card(id="total_countries", 
                                    card_label="Total countries operated in", 
                                    icon="bi bi-geo-alt-fill",
                                    style=cardstyling
                                    ),
                        output_card(id="total_cities", 
                                    card_label="Total number of cities operated in", 
                                    icon="bi bi-geo-fill",
                                    style=cardstyling
                                    )                       
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
                                        output_card(id="client_total_building", 
                                                    card_label="Total number of cities operated in", 
                                                    icon="bi bi-geo-fill",
                                                    style=cardstyling
                                                    ),
                                        output_card(id="client_total_building_area", 
                                                    card_label="Total number of cities operated in", 
                                                    icon="bi bi-geo-fill",
                                                    style=cardstyling
                                                    ),
                                        output_card(id="client_average_building_area", 
                                                    card_label="Total number of cities operated in", 
                                                    icon="bi bi-geo-fill",
                                                    style=cardstyling
                                                    )
                                    ]
                                ),
                                html.Br(),
                                dbc.Row(
                                    [
                                        output_card(id="client_total_points", 
                                                    card_label="Total Equipment Points", 
                                                    icon="bi bi-file-easel-fill",
                                                    style=cardstyling
                                                    ),
                                        output_card(id="client_total_equipment", 
                                                    card_label="Total Equipment", 
                                                    icon="bi bi-cpu-fill",
                                                    style=cardstyling
                                                    ),
                                        output_card(id="client_total_rooms", 
                                                    card_label="Total rooms", 
                                                    icon="bi bi-door-closed",
                                                    style=cardstyling
                                                    )
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
                                 output_card(id="bs_total_clients", 
                                            card_label="Total Clients", 
                                            icon="bi bi-people-fill",
                                            style=cardstyling
                                            ),
                                 output_card(id="bs_total_buildings", 
                                            card_label="Total Buildings", 
                                            icon="bi bi-house-fill",
                                            style=cardstyling
                                            ),
                                 output_card(id="bs_total_equipments", 
                                            card_label="Total Equipments", 
                                            icon="bi bi-cpu-fill",
                                            style=cardstyling
                                            )
                            ]
                        ),
                        html.Br(),
                        dbc.Row(
                            [
                                output_card(id="bs_total_equipment_points", 
                                            card_label="Total Equipment Points",
                                            icon="bi bi-grid-3x3-gap",
                                            style=cardstyling
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
                                        output_card(id="building_total_gateway", 
                                                    card_label="Number of ENVIO Gateways",
                                                    icon="bi bi-grid-3x3-gap",
                                                    style=cardstyling
                                                    ),
                                        output_card(id="total_building_devices", 
                                                    card_label="Total building Devices",
                                                    icon="bi bi-building",
                                                    style=cardstyling
                                                    ),
                                        output_card(id="gateway_per_unit_area", 
                                                    card_label="Gateway per Unit Area",
                                                    icon="bi bi-building",
                                                    style=cardstyling
                                                    )
                                    ]
                                ),
                                html.Br(),
                                dbc.Row(
                                    [
                                        output_card(id="device_per_unit_area", 
                                                    card_label="Device per unit Area",
                                                    icon="bi bi-building",
                                                    style=cardstyling
                                                    )
                           
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
        html.Br()
        
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
