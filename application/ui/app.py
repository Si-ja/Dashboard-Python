import dash
import dash_core_components as dcc
import dash_html_components as html 

from database_requests import DatabaseRequests
from graph_updater import generate_figure
from graph_updater import update_figure_range
from memory_container import MemoryKeeper

import pandas as pd 
import plotly.express as px

db_handler = DatabaseRequests()
tables_all = db_handler.get_ExistingTables()
tables_formated = db_handler.get_FormatedExistingTables()
columns_available = db_handler.get_FormatedExistingColumns(table_name=tables_all[0])
df = db_handler.get_Dataframe(table_name=tables_all[0])

# Update what we will keep in our memory
memoryKeeper = MemoryKeeper(dataframe=df, dataframe_name=tables_all[0])

# Generate a base figure
fig = generate_figure(dataframe_name=tables_all[0], variables=[columns_available[0]["value"]])

app = dash.Dash(__name__) 
app.layout = html.Div(children=[
    html.H1(
        children="Electricity Prices",
        style=dict(
            textAlign="center"
        )
    ),
    html.Div(
        dcc.Dropdown(
            id="Tables",
            options=tables_formated,
            value=tables_all[0],
            style={'width': '100%', 
                   'display': 'flex', 
                   'align-items': 'center', 
                   'justify-content': 'center', 
                   'padding': '10px'}
    )),
    html.Div(
        dcc.Dropdown(
            id="Columns",
            options=columns_available,
            value=columns_available[0]["value"],
            multi=True,
            style={'height': '100%', 
                   'width': '100%', 
                   'display': 'flex', 
                   'align-items': 'center', 
                   'justify-content': 'center', 
                   'padding': '10px'}
    )),
    html.Div(
        dcc.Graph(
            id='Time_Graph',
            figure=fig
        )
    ),
    html.H5(
        children="Chose a range, based on week ranges",
        style=dict(
            textAlign="center"
        )
    ),
    html.Div(
        dcc.RangeSlider(
            id="time_frame",
            min=1,
            max=memoryKeeper.time_period,
            step=None,
            marks=memoryKeeper.marks,
            value=[1, memoryKeeper.time_period],
        )
    )
])

# Make a callback to change the available columns to chose information from
@app.callback(
    dash.dependencies.Output(component_id="Columns", component_property="options"),
    [dash.dependencies.Input(component_id="Tables", component_property="value")])
def update_columns(input_data):
    columns_available = db_handler.get_FormatedExistingColumns(table_name=input_data)
    return columns_available

# Make a callback to reset the columns to chose from when the year chosen changes
@app.callback(
    dash.dependencies.Output(component_id="Columns", component_property="value"),
    [dash.dependencies.Input(component_id="Tables", component_property="value")])
def clean_columns(input_data):
    return columns_available[0]["value"]

# A call that is made when the amount of values in the columns dropdown changes
# Or when the table and its' year changes
# Or the period that we want to observer
# This calls to updating of the figure that is presented to the user
@app.callback(
    dash.dependencies.Output(component_id="Time_Graph", component_property="figure"),
    [dash.dependencies.Input(component_id="Columns", component_property="value"),
     dash.dependencies.Input(component_id="Tables", component_property="value"),
     dash.dependencies.Input(component_id="time_frame", component_property="value")])
def update_figure(_columns, _tables, new_range):
    # If the new graph is generated - then a new instance fully will be created
    # Otherwise only the old will be updated
    new_graph = False
    # See if we need to update our memory container
    if (str(memoryKeeper.name) != str(_tables)):
        temp_df = db_handler.get_Dataframe(table_name=_tables)
        memoryKeeper.name = memoryKeeper.setName(new_name=_tables)
        memoryKeeper.time_period= memoryKeeper.setDataframePeriod(new_dataframe=temp_df)
        memoryKeeper.marks = memoryKeeper.generateMarks()
        new_graph = True

    # Proceed to updating that part of information that will allow for display to change properly
    # If there is only 1 value, it will be treated as a string. If multiple, then as a list.
    # In the first case however, it needs to be converted into a list as well.
    if isinstance(_columns, str):
        _columns = [_columns]

    new_fig = None
    if new_graph:
        new_fig = generate_figure(dataframe_name=_tables, variables=_columns)
    else:
        # Update the observable range that needs to change
        new_fig = update_figure_range(dataframe_name=_tables, 
                                      variables=_columns, 
                                      dataframe_range=new_range)

    return new_fig


if __name__ == "__main__":
    app.run_server(debug=True)