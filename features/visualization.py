import pandas as pd
import plotly.express as px

# function to create boxplot
def make_boxplot(data: pd.DataFrame, variable_name: str):
    """This function accepts a data and variable name and returns a boxplot

    Args:
        data (pd.DataFrame): Data to visualize
        variable_name (str): variable to visualize with boxplot
    """
    data = data[[variable_name]].dropna()
    fig = px.box(data_frame=data, y = variable_name,
                 template='plotly_dark', height=700,
                 title = f'Boxplot to visualize outliers in {variable_name}'
                 )
    return fig
    
    
def plot_histogram(data: pd.DataFrame, colname: str):
    """Plot the distribution of variable using a histogram

    Args:
        data (pd.DataFrame): Data to use for plotting
        
        colname (str): column name or name of variable to plot 
    """
    data = data[[colname]].dropna()
    fig = px.histogram(data, x=colname, histnorm='probability density',
                       title=f'Distribution of {colname}',
                       height=700,
                       template='plotly_dark'
                       )
    return fig
