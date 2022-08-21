#%%
from venv import create
import dash_trich_components as dtc
from dash import dcc
import dash_bootstrap_components as dbc
from dash import html
from features.helper_components import output_card, output_card_alpha
from StyleDisplay.style import button_style

import pandas as pd

df = pd.read_csv(r'data/total_emission_df.csv')
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

model_card_style = {'borderColor': 'green',
                    'borderRadius': '70%',
                    'border': 'solid',
                    'textAlign': 'center',
                    'width': '30%',
                    'position': 'center',
                    #'textSize': '150%'
                    }

country_layout = html.Div(
    [
        dbc.Container(
            [
                html.H2('Average Carbon dioxide (CO2) emission of households'),
                dbc.Row(
                    [ output_card_alpha(loading_head_id='id_avg_all_emission', card_title='Average emission (all fuel type)'),
                        output_card_alpha(loading_head_id='id_avg_petrol_emission', card_title='Average emission (Petrol)'),
                        output_card_alpha(loading_head_id='id_avg_electricity_emission', card_title='Average emission (Electricity)'),
                        output_card_alpha(loading_head_id='id_avg_diesel_emission', card_title='Average emission (Diesel)')                        
                    ]
                ),
                html.Br(), html.Br(),
                dbc.Row(
                    [ output_card_alpha(loading_head_id='id_avg_lpg_emission', card_title='Average emission (LPG)'),
                        output_card_alpha(loading_head_id='id_avg_firewood_emission', card_title='Average emission (Firewood)'),
                        output_card_alpha(loading_head_id='id_avg_charcoal_emission', card_title='Average emission (Charcoal)'),
                        output_card_alpha(loading_head_id='id_avg_kerosene_emission', card_title='Average emission (Kerosene)')       
                    ]
                ),
                
                html.Br(), html.Br(),
                dbc.Row([dbc.Col(#lg=6, 
                                 children=[dbc.Label('Average Emission in each state'), 
                                            dcc.Graph(id='id_graph_bubble_country')
                                        ]
                                )
                         ]
                        ),
                html.Br(),
                dbc.Row([dbc.Col(lg=6,
                                 children=[dbc.Label('Histogram distribution'),
                                  dcc.Graph(id='id_graph_hist_country')
                                  ]
                                ),
                         dbc.Col(lg=6, 
                                 children=[dbc.Label('Boxplot of emission'), 
                                            dcc.Graph(id='id_graph_box_country')
                                        ]
                                )
                         ]
                        )
                
            ]
        )
    ]
)


sector_emission = html.Div(dbc.Container(
    [dbc.Row([dbc.Col(lg=4, 
                      children=[
                                dbc.Label('Select sector'), 
                                dcc.Dropdown(id='id_sector_dropdown',
                                            options=[{'label': sector, 'value': sector} 
                                                    for sector in df['sector'].unique()
                                                    ]
                                            )
                        ]
                    ),
              dbc.Col([output_card_alpha(loading_head_id='id_avg_sector_emission', 
                                         card_title='sector emission',
                                         )
                       ]
                      )
              ]
             ),
     html.Br(), html.Br(),
     dbc.Row([dbc.Col(lg=6, 
                      children=[dbc.Label('bubble chart emission for states in sector selected'),
                                dcc.Graph(id='id_graph_bubble_sector_state_emission')
                                ]
                    ),
              dbc.Col(lg=6, 
                      children=[dbc.Label('bubble for sector fuel type emission'),
                                dcc.Graph(id='id_graph_bubble_sector_fuel_emission')
                                ]
                    )
              ]
            )
     ]
    )
)


state_emission = dbc.Container(
    [
        html.Br(),
        dbc.Row(
            [
                dbc.Col(
                    lg=4,
                    children=[
                        dbc.Label("Select State"),
                        dcc.Dropdown(id='id_state_dropdown',
                                     options=[{'label': state, 'value': state} for state in df['state_name'].unique()]
                                    ),
                    ],
                ),
                dbc.Col(
                    lg=8,
                    children=[
                        dbc.Row(
                            [
                                dbc.Label(id='selected_state_emission'),
                                output_card_alpha(loading_head_id='id_avg_state_emission', card_title='Average emission')
                            ]
                        ),
                        html.Br(),
                    ],
                ),
            ]
        ),
        html.Br(),
        html.Br(),
        dbc.Row(
            [dbc.Col(lg=6, 
                     children=[dbc.Label('Histogram of emissions'), 
                               dcc.Graph(id='id_graph_hist_state')
                               ]
                     ), 
             dbc.Col(lg=6, children=[dbc.Label('Boxplot of state emission'), 
                                     dcc.Graph(id='id_graph_box_state')
                                     ]
                    )
            ]
        ),
        
        html.Br(),
        dbc.Row([dbc.Col(lg=6, children=[dbc.Label('Bubble chart of emission per fuel type in state'), 
                                         dcc.Graph(id='id_graph_bubble_state')
                                         ]
                         )
                 ]
                )
    ]
)

emission_prediction_layout = html.Div([dtc.SideBar([dtc.SideBarItem(id='desc_model_sidebutton', 
                                                                    label='Modelling process'
                                                                    ),
                                                    dtc.SideBarItem(id='eval_model_sidebutton',
                                                                    label='Models evaluation'
                                                                    ),
                                                    dtc.SideBarItem(id='model_predict_sidebutton',
                                                                    label='Prediction'
                                                                    )
                                                    ]
                                                   ),
                                        html.Div(id='prediction_content')
                                        ]
                                    )

model_description = html.Div([dcc.Markdown(""" ### Data preprocessing pipeline
                                           """
                                        )
                              ]
                             )


best_model_card = dbc.Card(children=[dbc.CardHeader('Best model: Hist'),
                            dbc.CardBody(children=[dbc.Col(#lg=6, 
                                                            children=[
                                                                        html.H5('Root Mean Squared Error (RMSE)'),
                                                                        html.H1('133',
                                                                                style=model_card_style
                                                                            ),
                                                                    ],
                                                            
                                                        ), 
                                                   html.Br(),
                                          
                                          dbc.Col(#lg=6, 
                                                  children=[
                                                            html.H5('Co-efficient of determination (R2)'),
                                                            html.Div(children=html.H1('23%'),
                                                                    style=model_card_style
                                                                    )
                                                        ]
                                            )
                                          ], 
                                         class_name='mx-auto'
                                         )
                            ],
                           color='light'
                        )





models_evaluated = dbc.Card([dbc.CardHeader('Models evaluated'),
                             dbc.CardBody([html.H3('Plot of RMSE of various models'),
                                           dcc.Graph(id='id_graph_models_rmse_plot')
                                           ]
                                          ),
                             dbc.CardFooter('R2 of models')
                             ]
                            )


model_evaluation = html.Div([
    dbc.Container([html.Br(),
                   dbc.Row([dbc.Col(lg=4, 
                                    children=[best_model_card]
                                    ), 
                            dbc.Col(lg=8,
                                    children=[models_evaluated])
                            ]
                        ), 
                   dbc.Row()
                   ]
                  )
    ]
)
'''
TO DO:
1. Sidebar
    i. Modelling process
    ii, Models

2. Main layout   
TO DO emission prediction:

1. dot plot of models evaluations: rmse
2. card for models evaluations: r2
3. card for best model: rmse, r2
'''

#############################

def create_dropdown(id: str, colname: str, data: pd.DataFrame):
    return dcc.Dropdown(id=id, options=[{'label': item, 'value': item} 
                                 for item in data[colname].unique()
                                 ]
                )
    
    
    
dcc.Dropdown(id='id_sector_dropdown',
            options=[{'label': sector, 'value': sector} 
                    for sector in df['sector']
                    ]
            )   
    
indicators_dropdowns = dbc.Container([dbc.Row(
                        children=[dbc.Col([create_dropdown(id='id_state_name', colname='state_name', data=df)]
                            ),
                        dbc.Col([create_dropdown(id='id_lga_name', colname='lga', data=df)]),
                        dbc.Col([create_dropdown(id='id_sector_name', colname='sector', data=df)])
                        ]
                    ),html.Br(), html.Br(),
               dbc.Row(children=[dbc.Col([dcc.Input(id='id_credit_amt', type='number', 
                                                    placeholder='select credit amount receive',
                                                    min=df['credit_mean'].min(),
                                                    max=df['credit_mean'].max(),
                                                    step=10, debounce=True
                                                    )
                                          ]
                                    ),
                                 
                                dbc.Col([dcc.Input(id='id_income_amt', type='number', 
                                                   placeholder='select income amount receive',
                                                    min=df['income_mean'].min(),
                                                    max=df['income_mean'].max(),
                                                    step=10, debounce=True, 
                                                    )
                                          ]
                                        ),
                                dbc.Col(dbc.Button(id='id_predict_emission',
                                                    children='Predict CO2 Emission',
                                                    style=button_style
                                                )
                                        )
                                ]
                    )
               ]
            )




prediction_board = dbc.Card([html.Br(), html.Br(),
                             dbc.CardHeader(children=indicators_dropdowns),
                            dbc.CardBody(children=[html.Div(html.H1('123'),
                                                    style=model_card_style
                                                )
                                            ],
                                            class_name='mx-auto'
                                            ),
                            dbc.CardFooter()
                            ]
                               )


model_prediction_show = html.Div([dbc.Container(
                                                [html.Br(), html.Br(),
                                                 dbc.Row(children=[prediction_board])
                                                 ]
                                                )
                                  ]
                                 )

'''
TO DO:
PREDICTION

1. Dropdowns with tooltip
    i. state
    ii. LGA
    iii. sector
    iv. credit
    v. income state
    vi. predict button
    
2. Prediction card
    i. cardheadr : prediction of co2
    ii. body: predict (2 d.p)
     
'''




hypothesis_layout = html.Div(
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

                                ### 


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

fuel_type_emission_layout = html.Div(
    [
        dbc.Container(
            [
                dbc.Row(
                    [
                        dbc.Col(lg=3, children=[dbc.Label('Select fuel type'), 
                                                dcc.Dropdown(id='id_fuel_type_dropdown',
                                                             options=[{'label': fuel_type, 'value': fuel_type}
                                                                      for fuel_type in ['kerosene', 'petrol', 'diesel', 'lgp',
                                                                                        'firewood', 'electricity', 'charcoal'
                                                                                        ]
                                                                      ]
                                                             )
                                                ],
                        ),
                        dbc.Col(lg=3, children=[dbc.Label('Select state'),dcc.Dropdown(id='id_state_fuel_dropdown',
                                                                                       options=[{'label': state, 'value': state} 
                                                                                                for state in df["state_name"].unique()
                                                                                                ]
                                                                                       )
                                                ]
                                ),
                        dbc.Col(lg=6, children=[output_card_alpha(loading_head_id='id_avg_fuel_emission',
                                                                  card_title='Average emission'
                                                                  ),
                                                ]
                                ),
                        
                    ]
                )
            ]
        ),
        html.Br(),
        html.Br(),
        dbc.Row([dbc.Col(lg=6, children=[dbc.Label('Histogram fuel carbon emission'), 
                          dcc.Graph(id='id_graph_hist_fuel')
                          ]
                         ),
                 dbc.Col(lg=6, children=[dbc.Label('Boxplot fuel emission'), 
                                         dcc.Graph(id='id_graph_box_fuel')
                                         ]
                         )
                 ]
                )
    ]
)



analytics_sidebar = html.Div(
    [
        dtc.SideBar(
            [
                dtc.SideBarItem(
                    id="id_country",
                    label="Country level",
                    icon="fas fa-infinity"
                ),
                dtc.SideBarItem(
                    id="id_state", label="State level", icon="fa fa-user-circle"
                ),
                dtc.SideBarItem(
                    id="id_sector", label="Sector level", icon="fas fa-chart-line"
                ),
                dtc.SideBarItem(
                    id='id_fuel',
                    label="Fuel type",
                    icon='bi bi-diagram-3-fill'
                ),
                dtc.SideBarItem(id="id_5", label="Metrics", icon="fas fa-cog"),
            ]
        ),
        html.Div([], id="page_content"),
    ]
)


'''
TO DO:
1. National level emission

** when component is hovered on, show number of households analyzed
** and method of analysis
-- Avg emission (all fuel)
-- Avg emission for electricity
-- Avg emission for LPG
-- Avg emission for FIREWOOD
-- Avg emission for charcoal
-- Avg emission for petrol
-- Avg emission for diesel
-- Avg emission for kerosene

II Histogram, boxplot for total emission
bubble plot for total emission in all states


2. State level

++ select state name

-- Avg state emission
-- max hh emission in state

III Histogram, boxplot for total state emission
bubble plot for state based on fuel type


3. Fuel type

++ Select fuel, state

-- Avg state fuel type emission
-- max hh emission in state

IV Histogram, boxplot for total state fuel type emission
Bubble chart per fuel for all states






'''