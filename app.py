from dash import html, Input, Output, State, dcc
import dash_bootstrap_components as dbc
import pandas as pd
from dash.exceptions import PreventUpdate
from features.helper_components import (main_layout
                                        )
from features.pages import create_page_with_card_button
from features.pages_show import (analytics_sidebar, 
                                 emission_prediction_layout, 
                                 hypothesis_layout
                                 )
import dash
from StyleDisplay.style import homepage_icon_style

import logging
from urllib.parse import unquote
import joblib
import functools
import plotly.express as px
import server

app_description = create_page_with_card_button()
#%%
app = dash.Dash(__name__, external_stylesheets=[
                                                dbc.themes.SOLAR,
                                                dbc.icons.BOOTSTRAP,
                                                dbc.icons.FONT_AWESOME
                                            ],
                suppress_callback_exceptions=True,
                )

app.layout = main_layout

app.validation_layout = html.Div(
    [main_layout, 
     #create_page_with_card_button()
     #explore_layout, 
     app_description, 
     analytics_sidebar,
     emission_prediction_layout
     #prediction_layout, 
     #histogram_layout,
     #scatter_layout, boxplot_layout, 
     #multicoll_layout, intro_layout
     ]
)





#if '__name__' == '__main__':
#app.run_server(port=8084, debug=False)


if __name__=='__main__':
    app.run_server(port=8080, debug=False, use_reloader=False)