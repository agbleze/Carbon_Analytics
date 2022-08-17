from dash import Input, Output, State, callback
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
from features.pages_show import (analytics_layout, 
                                 carbon_emission, 
                                 hypothesis_layout
                                 )


@callback(
    Output(component_id="main_content", component_property="children"),
    Input(component_id="location", component_property="href"),
)
def show_page_display(href):
    site_page = href
    site_to_view = site_page.split("/")[-1]
    if site_to_view == "carbon_analytics":
        return analytics_layout 
    elif site_to_view == 'emission_prediction':
        return carbon_emission
    elif site_to_view == 'hypothesis':
        return hypothesis_layout
    else:
        return app_description