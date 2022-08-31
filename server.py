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
                                 fuel_type_emission_layout,
                                 state_emission,
                                 sector_emission,
                                 model_description,
                                 model_evaluation,
                                 model_prediction_show
                                 
                                 )
from features.visualization import (make_boxplot, plot_histogram, plot_bubble_chart)
from models.models_evaluation import  plot_models_cv_test_error
import pandas as pd
from datar.all import case_when, f, mutate, pivot_wider
import functools
from models.Co2XgbrfRegressor import xgb_pipeline

from models.preprocess_pipeline import (X, y
                                        )

import joblib
import pandas as pd

#%%
loaded_model = joblib.load("model_used.model")

#loaded_model = joblib.load(filename='/home/linagb/Carbon_Analytics/model_used.model')

#%%
fuel_type_emission = pd.read_csv('data/fuel_type_emission.csv')
total_emission_df = pd.read_csv('data/total_emission_df.csv')

#fuel_type_emission = pd.read_csv(r'/home/linagb/Carbon_Analytics/data/fuel_type_emission.csv')
#total_emission_df = pd.read_csv(r'/home/linagb/Carbon_Analytics/data/total_emission_df.csv')


fuel_type_emission_long = pd.melt(fuel_type_emission,id_vars=['state_name', 'sector', 'lga'], 
                                    value_vars=['petrol', 'kerosene','lpg', 
                                                'electricity',	'charcoal',	
                                                'diesel', 'firewood'
                                                ], 
                                    var_name='fuel_type', 
                                    value_name='total_emission'
                                    )


#%%
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
        return fuel_type_emission_layout
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
          Output(component_id='id_avg_electricity_emission', component_property='children'),
          Output(component_id='id_avg_diesel_emission', component_property='children'),
          Output(component_id='id_avg_lpg_emission', component_property='children'),
          Output(component_id='id_avg_firewood_emission', component_property='children'),
          Output(component_id='id_avg_charcoal_emission', component_property='children'),
          Output(component_id='id_avg_kerosene_emission', component_property='children'),
          Output(component_id='id_avg_all_emission', component_property='children'),
          Output(component_id='id_graph_hist_country', component_property='figure'),
          Output(component_id='id_graph_box_country', component_property='figure'),
          Output(component_id='id_graph_bubble_country', component_property='figure'),
          Input(component_id='id_country', component_property='n_clicks_timestamp')
          )
def render_country_emission(country_button):
    ctx = callback_context
    button_clicked = ctx.triggered[0]['prop_id'].split('.')[0]
    
    if button_clicked != 'id_country':
        PreventUpdate
        
    avg_petrol_emission = fuel_type_emission['petrol'].mean()
    avg_electricity_emission = fuel_type_emission['electricity'].mean()
    avg_diesel_emission = fuel_type_emission['diesel'].mean()
    avg_lpg_emission = fuel_type_emission['lpg'].mean()
    avg_firewood_emission = fuel_type_emission['firewood'].mean()
    avg_charcoal_emission = fuel_type_emission['charcoal'].mean()
    avg_kerosene_emission = fuel_type_emission['kerosene'].mean()
    avg_all_emission = total_emission_df['total_CO2_kg'].mean()
    
    avg_emission_per_state = total_emission_df.groupby('state_name')['total_CO2_kg'].mean().reset_index()
    
    country_hist_graph = plot_histogram(data=total_emission_df, colname='total_CO2_kg')
    country_box_graph = make_boxplot(data=total_emission_df, variable_name='total_CO2_kg')
    country_bubble_graph = plot_bubble_chart(data=avg_emission_per_state, x_axis='state_name',
                                            y_axis='total_CO2_kg',
                                            bubble_size='total_CO2_kg',
                                            title='Average emission in each state in Nigeria'
                                        )
    
    return (round(avg_petrol_emission, 2),
            round(avg_electricity_emission, 2),
            round(avg_diesel_emission, 2),
            round(avg_lpg_emission, 2),
            round(avg_firewood_emission, 2),
            round(avg_charcoal_emission, 2),
            round(avg_kerosene_emission, 2),
            round(avg_all_emission, 2),
            country_hist_graph,
            country_box_graph,
            country_bubble_graph
            )
    


@callback(Output(component_id='id_avg_state_emission', component_property='children'),
          Output(component_id='id_graph_hist_state', component_property='figure'),
          Output(component_id='id_graph_box_state', component_property='figure'),
          Output(component_id='id_graph_bubble_state', component_property='figure'),
          Input(component_id='id_state_dropdown', component_property='value')
          )
def render_state_emission(state_selected):
    state_emission = total_emission_df[total_emission_df['state_name']==state_selected]#['total_CO2_kg'].mean()
    fuel_type_emit = (fuel_type_emission_long[fuel_type_emission_long['state_name']==state_selected]
                      .groupby(['fuel_type'])['total_emission'].mean().reset_index()
                      )
    fuel_type_emit.rename(columns={'total_emission': 'average_co2_emission'}, inplace=True)
    avg_state_emission = state_emission['total_CO2_kg'].mean()
    graph_hist_state = plot_histogram(data=state_emission, colname='total_CO2_kg')
    graph_box_state = make_boxplot(data=state_emission, variable_name='total_CO2_kg')
    graph_bubble_state = plot_bubble_chart(data=fuel_type_emit, x_axis='fuel_type', 
                                           y_axis='average_co2_emission', 
                                            bubble_size='average_co2_emission', 
                                            title=f'Average Co2 emission in {state_selected} per fuel type'
                                            )
    return (round(avg_state_emission, 2), 
            graph_hist_state, 
            graph_box_state,
            graph_bubble_state
            )



#%%
@callback(Output(component_id='id_avg_fuel_emission', component_property='children'),
          Output(component_id='id_graph_hist_fuel', component_property='figure'),
          Output(component_id='id_graph_box_fuel', component_property='figure'),
          Input(component_id='id_fuel_type_dropdown', component_property='value'),
          Input(component_id='id_state_fuel_dropdown', component_property='value'),
          Input(component_id='id_fuel', component_property='n_clicks_timestamp')
          )
def render_fuel_type(fuel_selected, state_selected, fuel_sidebar_button):
    ctx = callback_context
    button_clicked = ctx.triggered[0]['prop_id'].split('.')[0]
    
    if (not fuel_selected) or (not state_selected) or  button_clicked != 'id_fuel':
        PreventUpdate
    
    data_selected = fuel_type_emission_long[(fuel_type_emission_long['state_name']==state_selected) & 
                            (fuel_type_emission_long['fuel_type']==fuel_selected)
                            ]   
    
    avg_fuel_emission = data_selected[['total_emission']].mean() 
    #avg_fuel_emission.rename(columns={'total_emission': 'Average Co2 emission (kg)'}, inplace=True)
    graph_hist_fuel = plot_histogram(data=data_selected, colname='total_emission')
    graph_box_fuel = make_boxplot(data=data_selected, variable_name='total_emission')
    
    return (round(avg_fuel_emission, 2),
            graph_hist_fuel,
            graph_box_fuel
            )


@callback(Output(component_id='id_avg_sector_emission', component_property='children'),
          Output(component_id='id_graph_bubble_sector_state_emission', component_property='figure'),
          Output(component_id='id_graph_bubble_sector_fuel_emission', component_property='figure'),
          Input(component_id='id_sector_dropdown', component_property='value'),
          Input(component_id='id_sector', component_property='n_clicks_timestamp')
          )
def render_sector_layout(sector_selected, sector_sidebar_button):
    ctx = callback_context
    button_clicked = ctx.triggered[0]['prop_id'].split('.')[0]
    
    if (not sector_selected) or (button_clicked != 'id_sector'):
        PreventUpdate
    
    sector_data = fuel_type_emission_long[fuel_type_emission_long['sector'] == sector_selected]
    
    avg_sector_emission = sector_data['total_emission'].mean()
    avg_sector_state_df = sector_data.groupby('state_name')['total_emission'].mean().reset_index()
    avg_sector_fuel_df = sector_data.groupby('fuel_type')['total_emission'].mean().reset_index()

    graph_sector_state = plot_bubble_chart(data=avg_sector_state_df, x_axis='state_name',
                                            y_axis='total_emission', bubble_size='total_emission',
                                            title=f'Average co2 emission (kg) per {sector_selected} states'
                                            )
    
    graph_sector_fuel = plot_bubble_chart(data=avg_sector_fuel_df, x_axis='fuel_type',
                                            y_axis='total_emission', bubble_size='total_emission',
                                            title=f'Average co2 emission (kg) per fuel type in {sector_selected}'
                                            )
    
    return (round(avg_sector_emission, 2), 
            graph_sector_state, 
            graph_sector_fuel
            )



@callback(Output(component_id='id_graph_avg_cv_rmse_plot', component_property='figure'),
          Output(component_id='id_graph_models_rmse_plot', component_property='figure'),
          Input(component_id='eval_model_sidebutton', component_property='n_clicks_timestamp')
          )
@functools.lru_cache(maxsize=None)
def plot_models_error_estimates(sidebar_button):
    ctx = callback_context
    button_clicked = ctx.triggered[0]['prop_id'].split('.')[0]
    if (not button_clicked) or (button_clicked != 'eval_model_sidebutton'):
        PreventUpdate
    test_rmse_graph = plot_models_cv_test_error()
    cv_test_rmse_graph = test_rmse_graph['test_rmse']#.show()
    avg_test_rmse = test_rmse_graph['avg_test_rmse']#.show()
    
    return (avg_test_rmse, cv_test_rmse_graph)
        
    
@callback(Output(component_id='prediction_results', component_property='children'),
          Output(component_id='id_prediction_describe', component_property='children'),
          Input(component_id='id_state_name', component_property='value'),
          Input(component_id='id_lga_name', component_property='value'),
          Input(component_id='id_sector_name', component_property='value'),
          Input(component_id='id_credit_amt', component_property='value'),
          Input(component_id='id_income_amt', component_property='value'),
          Input(component_id='id_predict_emission', component_property='n_clicks_timestamp')
          )
def make_prediction(state_selected, lga_selected, sector_selected, credit_amt, 
                    income_amt, predict_button):
    ctx = callback_context
    button_clicked = ctx.triggered[0]['prop_id'].split('.')[0]
    
    # prediction_input = [state_selected, lga_selected, sector_selected, credit_amt,
    #                     income_amt]
    
    
    
    prediction_inputs = {'state_name': state_selected, 'lga': lga_selected, 
                         'sector': sector_selected, 'credit_mean': credit_amt, 
                         'income_mean': income_amt
                         }
    prediction_inputs_df = pd.DataFrame(data=prediction_inputs, index=[0])

    
    if ((not button_clicked) or (button_clicked != 'id_predict_emission') 
        or (not any(prediction_inputs_df)) or (not predict_button)
        ):
        PreventUpdate
        
    if button_clicked == 'id_predict_emission':
        
        if not all(prediction_inputs_df):
            PreventUpdate
            
            # message = ('All parameters must be provided. Either some values have not \
            #             been provided or invalid values were provided. Please select the \
            #            right values for all parameters from the dropdown. \
            #             Then, click on predict clicks button to \
            #             predict number of clicks'
            #            )
            # return True, message, dash.no_update
        
        if all(prediction_inputs_df):
            result = loaded_model.predict(prediction_inputs_df)[0]
            prediction = round(result)
            prediction_desc = f'Household with the selected characteristics is predicted to emit {prediction} kg carbon dioxide'
            return (prediction, prediction_desc) #False, dash.no_update, prediction
        
        
        #%%
# import pandas as pd
# dat = {'state_name': 'kano', 'lga': 123, 'sector': 'RURAL', 'credit_mean': 123, 'income_mean': 120}
# input_pred = pd.DataFrame(data=dat, index=[0])
# #pd.DataFrame.from_dict(data=dat)

# # %%
# xgb_pipeline.predict(input_pred)[0]


            
    
    #xgb_pipeline.fit(X=X, y=y)

    #prediction = xgb_pipeline.predict([prediction_input])
    #return f'{prediction: .2f}'

    
    
    
    