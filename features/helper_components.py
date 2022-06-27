from dash import dcc, html
import dash_bootstrap_components as dbc
from StyleDisplay.style import (cardbody_style, 
                                 card_icon, cardimg_style, 
                                 card_style,
                                 page_style,
                                 outputcard_style,
                                 popover_head_style)



def output_card(id: str = None, card_label: str =None,
                style={"backgroundColor": 'yellow'},
                icon: str ='bi bi-cash-coin', card_size: int = 4):
    return dbc.Col(lg=card_size,
                    children=dbc.CardGroup(
                        children=[
                            dbc.Card(
                                    children=[
                                        html.H3(id=id),
                                        html.P(card_label)
                                    ]
                                ),
                            dbc.Card(
                                    children=[
                                        html.Div(
                                            className=icon,
                                            style=card_icon
                                        )
                                    ],
                                    style=style
                            )
                        ]
                    )
                )


def create_offcanvans(id: str, title: str, is_open=False):
    return html.Div(
        [
            dbc.Offcanvas(
                id=id,
                title=title,
                is_open=is_open,
                children=[
                    dcc.Markdown('''
                                    #### Project description

                                    The aim of this project is to predict the number of days that
                                    customers are likely to book an accommodation for based on user bahaviour.
                                    The client is an accommodation provider who sought to obtain
                                    an intelligent tool that can enable the prediction of booking days
                                    based on a number of features.

                                    #### Features / variables used

                                    The dataset had a number of variables used as predictors for
                                    predicting number of accommodations booked as the target variable.
                                    These includes the following;

                                    ##### Predictor variables
                                    __Number of sessions__ : This describes the number of sessions a customer made
                                    on the booking site.

                                    __City__ : This is the city from which a customer is accessing the booking site from

                                    __Country__ : This is the country from which the user is accessing the booking site.
                                    During the selection of various variables, you do not have the burden to decide this
                                    as reference is automatically made from the city selected.

                                    __Device Class__ : This is the type of device used to access the booking site. It has
                                    the values desktop, phone or tablet

                                    __Instant Booking__ : The is a feature on a booking site. Whether or not this
                                    feature was used by a customer is included in predicting the number of day to
                                    be booked

                                    __User Verification Status__ : Whether or not a customer who visited the site
                                    has been verified is included in predicting number of days to be booked.

                                    ##### Target variable
                                    __ Number of accommodation days to be booked__


                                    #### Tools and method used
                                    Automated machine learning (AutoML) was employed to deliver a high
                                    accuracy optimized prediction model. The model is used to create
                                    an API that receives request, makes and send prediction as response
                                    to this web application.

                                    With the user interface provided here, various features describing customers
                                    behaviours and attributes can be selected to make a prediction.

                                    Among others, the tools used included the following

                                    * TPOT as an AutoML package to develop the machine learning model
                                    * Dash to build this web application as the User Interface
                                    * Flask to develop the API for the machine learning model


                                    #### Project output

                                    The main output of this project were the following

                                    * Machine learning API deployed
                                    * Machine learning web application



                                '''
                                )
                    ]
            ),
        ]
    )


main_layout = html.Div(
    [
        dbc.NavbarSimple(
            brand="Carbon Analytics",
            brand_href="/",
            light=True,
            brand_style={"color": "#FFFFFF", "backgroundColor": "#2F4F4F"},
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        dcc.Location(id="location"),
                        html.Div(id="main_content"),
                        dcc.Loading(
                            id="loading_cach_data_stored",
                            type="cube",
                            fullscreen=True,
                            children=[dcc.Store(id="cach_data_stored")
                                      ],
                        ),
                    ]
                )
            ]
        ),
    ],
    style=page_style,
)




def output_card_alpha(col_id: str = 'col_id_test',
                      loading_id: str = 'loading_id_test',
                      loading_type="circle", 
                      loading_head_id: str = "loading_head_id",
                      card_title: str = 'card_title',
                      icon: str = "fas fa-toolbox",
                      card_style: str = outputcard_style,
                      popover_head: str = 'Heading of popover',
                      popover_head_style: dict = popover_head_style,
                      popover_body_style: dict = None,
                      analysis_method: str = "This details the analysis approach",
                      target_id: str = "target_id_test",
                      trigger_type: str = "hover",
                      popover_body_topic: str = "Analysis Method"
                      
                      ):

    output_card = dbc.Col(
            id=col_id,
            children=[
                dbc.CardGroup(
                    [
                        dbc.Card(
                            dbc.CardBody(
                                [
                                    dcc.Loading(
                                        id=loading_id,
                                        type=loading_type,
                                        children=[
                                            html.H2(
                                                id=loading_head_id,
                                                className="card-title",
                                            )
                                        ],
                                    ),
                                    html.P(
                                        children=card_title,
                                        className="card-text",
                                    ),
                                ]
                            )
                        ),
                        dbc.Card(
                            html.Div(
                                className=icon,
                                style=card_icon,
                            ),
                            style=card_style,
                        ),
                    ]
                ),
                dbc.Popover(
                    [
                        dbc.PopoverHeader(
                            [
                                html.H5(
                                    popover_head
                                )
                            ],
                            style=popover_head_style,
                        ),
                        dbc.PopoverBody(
                            [ 
                                html.H6(
                                    popover_body_topic
                                ),
                                html.P(
                                    analysis_method
                                ),
                            ],
                            style=popover_body_style,
                        ),
                    ],
                    target=target_id,
                    trigger=trigger_type,
                ),
            ],
        )
    
    return output_card



