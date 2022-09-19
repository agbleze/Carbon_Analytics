#%%
from venv import create
import dash_trich_components as dtc
from dash import dcc
import dash_bootstrap_components as dbc
from dash import html
from features.helper_components import output_card, output_card_alpha
from features.feacture_component import CardButton
from StyleDisplay.style import button_style

import pandas as pd

df = pd.read_csv(r'data/total_emission_df.csv')

from PIL import Image

#%%
img_rmse = Image.open('pic/cv_rmse_long.png')
img_avg_cv_rmse = Image.open('pic/avg_cv_rmse_long.png')


#img_rmse = Image.open('/home/linagb/Carbon_Analytics/pic/cv_rmse_long.png')
#img_avg_cv_rmse = Image.open('/home/linagb/Carbon_Analytics/pic/avg_cv_rmse_long.png')


#df = pd.read_csv(r'/home/linagb/Carbon_Analytics/data/total_emission_df.csv')
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

emission_prediction_layout = html.Div([dtc.SideBar([
                                                    dtc.SideBarItem(id='desc_model_sidebutton', 
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


model_description = dbc.Container([dcc.Markdown(""" ### Data preprocessing pipeline
                                                Different machine larning algorithmns were fitted on the data and evaluated 
                                                using 10 fold cross validation method to determine the best model.
                                                
                                                Different algorithmns require some differences in preprocessing.
                                                
                                                1. Missing data was handled using mean imputation. Other methods of handling
                                                 missing data may prove more useful in modelling the data This step was part 
                                                 of the preprocessing pipeline for all algorithmns
                                                 
                                                2. Standardization of quantitative variables such as credit amount and income amount 
                                                This was done for linear models such as Lasso and ridge regression
                                                
                                                3. One-Hot-encoding for transforming qualitative variables was undertaken for linear models 
                                                such as Lasso and ridge regression.
                                                
                                                4. Ordinal encoding was used for transforming qualitative variables for decision tree 
                                                based models
                                                
                                                """
                                                )
                                    ]
                                )






# best_model_card = dbc.Card(children=[dbc.CardHeader('Best model: Hist'),
#                             dbc.CardBody(children=[dbc.Col(#lg=6, 
#                                                             children=[
#                                                                         html.H5('Root Mean Squared Error (RMSE)'),
#                                                                         html.H1('133',
#                                                                                 style=model_card_style
#                                                                             ),
#                                                                     ],
                                                            
#                                                         ), 
#                                                    html.Br(),
                                          
#                                           dbc.Col(#lg=6, 
#                                                   children=[
#                                                             html.H5('Co-efficient of determination (R2)'),
#                                                             html.Div(children=html.H1('23%'),
#                                                                     style=model_card_style
#                                                                     )
#                                                         ]
#                                             )
#                                           ], 
#                                          class_name='mx-auto'
#                                          )
#                             ],
#                            color='light'
#                         )



models_rmse_evaluated = dbc.Card([dbc.CardHeader('Evaluation of Models'),
                                    dbc.CardBody([html.H3('Boxplot of test RMSE of various models'),
                                                # dcc.Loading(type='circle',
                                                #             children=[dcc.Graph(id='id_graph_models_rmse_plot'),
                                                                      
                                                #                       ]
                                                #             ),
                                                
                                                dbc.CardImg(id='img_rmse',
                                                            src=img_rmse
                                                                #src=img_explore,
                                                                #top=True,
                                                                #style=homepage_icon_style,
                                                            
                                                            )
                                                ]
                                                ),
                                    dbc.CardFooter('Boxplot of test RMSE for 10 fold CV of various models')
                                ]
                            )


average_rmse_evaluated = dbc.Card([dbc.CardHeader('Average of 10 fold CV RMSE'),
                             dbc.CardBody([html.H3('Average RMSE of various models'),
                                        #    dcc.Loading(type='circle',
                                        #                children=[dcc.Graph(id='id_graph_avg_cv_rmse_plot'),
                                                                 
                                        #                          ]
                                        #                ),
                                        
                                            dbc.CardImg(id='img_avg_cv_rmse', 
                                                        src=img_avg_cv_rmse
                                            #src=img_explore,
                                            #top=True,
                                            #style=homepage_icon_style,
                                        )
                                                    
                                           
                                           ]
                                          ),
                             dbc.CardFooter('Averages of 10 fold CV test RMSE of various models')
                             ]
                            )


model_evaluation = dbc.Container([html.Br(), #html.Div([
                   dbc.Row([dbc.Col(#lg=6, 
                                    children=[models_rmse_evaluated]
                                    ), 
                            html.Br(), html.Br(),
                            
                            #dbc.Col(id='img_rmse'),
                            # dbc.Col(
                                    dbc.CardImg(id='img_rmse'
                                            #src=img_explore,
                                            #top=True,
                                            #style=homepage_icon_style,
                                        )
                            # )
                            
                            ]
                        ), html.Br(), html.Br(),  
                   dbc.Row([dbc.Col(#lg=6,
                                    children=[average_rmse_evaluated]
                                    ),
                            html.Br(), #html.Br(),
                            #dbc.Col(id='img_avg_cv_rmse'),
                            # dbc.Col(
                                    # dbc.CardImg(id='img_avg_cv_rmse'
                                    #         #src=img_explore,
                                    #         #top=True,
                                    #         #style=homepage_icon_style,
                                    #     )
                            # )
                       
                   ])
                   ]
                  )
 #   ]
#)

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
                                                children=[dbc.Col([dbc.Label('Select name of state'),
                                                                create_dropdown(id='id_state_name', colname='state_name', data=df)
                                                                ]
                                                                ),
                                                            dbc.Col([dbc.Label('Select Local Government Area'),
                                                                    create_dropdown(id='id_lga_name', colname='lga', data=df)]),
                                                            dbc.Col([dbc.Label('Select sector of household'),
                                                                    create_dropdown(id='id_sector_name', colname='sector', data=df)])
                                                        ]
                                            ),
                                            html.Br(), html.Br(),
                                dbc.Row(children=[dbc.Col(lg=4, children=[dbc.Label('Select credit amount Household receive'),
                                                                            dcc.Input(id='id_credit_amt', type='number', 
                                                                                        min=df['credit_mean'].min(),
                                                                                        max=df['credit_mean'].max(),
                                                                                        step=10, debounce=True
                                                                                        )
                                                                            ]
                                                            ),
                                 
                                dbc.Col(lg=4, children=[dbc.Label('Select income amount household receive'),
                                                        dcc.Input(id='id_income_amt', type='number',
                                                                    min=df['income_mean'].min(),
                                                                    max=df['income_mean'].max(),
                                                                    step=10, debounce=True, 
                                                                )
                                                            ]
                                        ),
                                dbc.Col(lg=4, children=[dbc.Button(id='id_predict_emission',
                                                        children='Predict CO2 Emission',
                                                        style=button_style
                                                        )
                                                        ]
                                        )
                                ]
                    )
               ]
            )




prediction_board = dbc.Card([html.Br(), #html.Br(),
                             dbc.CardHeader(children=indicators_dropdowns), html.Br(),
                            # dbc.CardBody(children=[html.Div(html.H1(id='prediction_results'),
                            #                         style=model_card_style
                            #                     )
                            #                 ],
                            #                 class_name='mx-auto'
                            #                 ),
                            dbc.CardBody(
                                        children=CardButton(id_card_body='prediction_results',
                                                            card_style = {"width": "9rem", "height": "8rem"}
                                                    ),
                                        class_name='mx-auto'
                                    ),
                            # output_card(id='prediction_results'),
                            html.Br(),

                            dbc.CardFooter(id='id_prediction_describe')
                            ]
                               )


#CardButton(id_card_body='prediction_results')


model_prediction_show = html.Div([dbc.Container(
                                                [html.Br(), html.Br(),
                                                 dbc.Row(children=[prediction_board])
                                                 ]
                                                )
                                  ]
                                 )

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
                #dtc.SideBarItem(id="id_5", label="Metrics", icon="fas fa-cog"),
            ]
        ),
        html.Div([], id="page_content"),
    ]
)
