def generate_figure(dataframe_name, variables):
    """
    Generate a figure with all of the needed parameters. 

    Input:
        dataframe(pd.Dataframe) - pandas dataframe from which the data needs to be generated
        varialbes - all the varialbe names that need to processed into a graph. Should be a list.
                    By default, will only include one variable otherwise.

    Output:
        fig - figure that can be plotted.
    """
    from database_requests import DatabaseRequests
    import plotly.graph_objects as go
    import pandas as pd

    # Prepare the needed dataframe
    db_handler = DatabaseRequests()
    df = db_handler.get_Dataframe(table_name=dataframe_name)

    # Do initial preparation of what will be the time representation and the figure holding variable
    # It is assumed that the time will always be the  first variable irregardless of it's name
    x = df.iloc[:,0] 
    fig = go.Figure()

    # Itterate through the list of variables to add to the graph and include them
    for inclusion in variables:
        fig.add_trace(go.Scatter(
            x=x,
            y=df[str(inclusion)],
            name=str(inclusion),
            connectgaps=True #In case there are any historical gaps - we want to fill them in
        ))
    return fig

def update_figure_range(dataframe_name, variables, dataframe_range):
    """
    Generate a figure with all of the needed parameters. And a specific range change.

    Input:
        dataframe(pd.Dataframe) - pandas dataframe from which the data needs to be generated
        varialbes - all the varialbe names that need to processed into a graph. Should be a list.
                    By default, will only include one variable otherwise.
        dataframe_range(list) - a range that will have to be displayed to the user.

    Output:
        fig - figure that can be plotted.
    """
    from database_requests import DatabaseRequests
    import plotly.graph_objects as go
    import pandas as pd

    # Prepare the needed dataframe
    db_handler = DatabaseRequests()
    df = db_handler.get_Dataframe(table_name=dataframe_name)

    # Do initial preparation of what will be the time representation and the figure holding variable
    # It is assumed that the time will always be the  first variable irregardless of it's name
    x = df.iloc[dataframe_range[0] -1: dataframe_range[1],0]
    fig = go.Figure()

    # Itterate through the list of variables to add to the graph and include them
    for inclusion in variables:
        fig.add_trace(go.Scatter(
            x=x,
            y=df[str(inclusion)],
            name=str(inclusion),
            connectgaps=True #In case there are any historical gaps - we want to fill them in
        ))
    return fig