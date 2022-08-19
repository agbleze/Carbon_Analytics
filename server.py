from dash import Input, Output, State, callback, callback_context
from dash.exceptions import PreventUpdate

from dash.exceptions import PreventUpdate
from features.helper_components import (main_layout
                               #plot_histogram, 
                               #plot_scatterplot, 
                               #make_boxplot, 
                               #CorrelationMatrix, plot_histogram, 
                               #plot_scatterplot, make_boxplot
                               )
from features.pages import create_page_with_card_button
from features.pages_show import (analytics_sidebar, 
                                 emission_prediction_layout, 
                                 hypothesis_layout,
                                 country_layout,
                                 fuel_type_emission,
                                 state_emission,
                                 sector_emission,
                                 model_description,
                                 model_evaluation,
                                 model_prediction_show
                                 
                                 )

import pandas as pd

fuel_type_emission = pd.read_csv('data/fuel_type_emission.csv')

app_description = create_page_with_card_button()


@callback(
    Output(component_id="main_content", component_property="children"),
    Input(component_id="location", component_property="href"),
)
def show_page_display(href):
    site_page = href
    site_to_view = site_page.split("/")[-1]
    if site_to_view == "carbon_analytics":
        return analytics_sidebar 
    elif site_to_view == 'emission_prediction':
        return emission_prediction_layout
    elif site_to_view == 'hypothesis':
        return hypothesis_layout
    else:
        return app_description
    

@callback(Output(component_id='page_content', component_property='children'),
          Input(component_id='id_country', component_property='n_clicks_timestamp'),
          Input(component_id='id_state', component_property='n_clicks_timestamp'),
          Input(component_id='id_fuel', component_property='n_clicks_timestamp'),
          Input(component_id='id_sector', component_property='n_clicks_timestamp')
          )
def render_country_layout(country_button_click, state_button_click, 
                          fuel_button, sector_button
                        ):
    ctx = callback_context
    button_clicked = ctx.triggered[0]["prop_id"].split(".")[0]
    
    if button_clicked == 'id_country':
        return country_layout
    elif button_clicked == 'id_state':
        return state_emission
    elif button_clicked == 'id_fuel':
        return fuel_type_emission
    elif button_clicked == 'id_sector':
        return sector_emission


@callback(Output(component_id='prediction_content', component_property='children'),
          Input(component_id='desc_model_sidebutton', component_property='n_clicks_timestamp'),
          Input(component_id='eval_model_sidebutton', component_property='n_clicks_timestamp'),
          Input(component_id='model_predict_sidebutton', component_property='n_clicks_timestamp')
          )
def render_prediction_layout(desc_model_button, eval_model_button, model_predict_button):
    ctx = callback_context
    button_clicked = ctx.triggered[0]['prop_id'].split('.')[0]
    if not button_clicked:
        PreventUpdate
    elif button_clicked == 'desc_model_sidebutton':
        return model_description
    elif button_clicked == 'eval_model_sidebutton':
        return model_evaluation
    elif button_clicked == 'model_predict_sidebutton':
        return model_prediction_show
    
    
@callback(Output(component_id='id_avg_petrol_emission', component_property='children'),
          Input(component_id='id_country', component_property='n_clicks_timestamp'))
def render_country_emission(country_button):
    ctx = callback_context
    button_clicked = ctx.triggered[0]['prop_id'].split('.')[0]
    
    if button_clicked != 'id_country':
        PreventUpdate
        
    avg_petrol_emission = fuel_type_emission['petrol'].mean()
    
    return round(avg_petrol_emission, 2)
    
