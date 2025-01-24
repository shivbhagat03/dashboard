import dash #type:ignore
import dash_core_components as dcc  #type:ignore
import dash_html_components as html #type:ignore
from config import FIELDS

def create_layout(app):
    app.layout = html.Div([
        html.Div([
            html.Div([
                html.Label("Start Datetime (YYYY-MM-DDTHH:MM:SS):"),
                dcc.Input(
                    id='start-datetime-input',
                    type='text',
                    placeholder="Enter start datetime",
                    value="2016-01-11T05:00:00",
                    style={"width": "100%"}
                ),
            ], style={"width": "40%", "marginRight": "10px"}),
            html.Div([
                html.Label("End Datetime (YYYY-MM-DDTHH:MM:SS):"),
                dcc.Input(
                    id='end-datetime-input',
                    type='text',
                    placeholder="Enter end datetime",
                    value="2016-03-09T08:00:00",
                    style={"width": "100%"}
                ),
            ], style={"width": "45%", "marginLeft": "10px"}),
        ], style={"display": "flex", "alignItems": "center", "marginBottom": "20px"}),

        html.Div([
            html.Div([
                html.Label("Select Field:"),
                dcc.Dropdown(
                    id='field-dropdown',
                    options=[{'label': field, 'value': field} for field in FIELDS],
                    value='T1',
                    placeholder="Select a field to visualize",
                    style={"width": "100%"}
                ),
            ], style={"width": "30%", "marginRight": "10px"}),

            html.Div([
                html.Label("Threshold Value:"),
                dcc.Input(
                    id='threshold-value-input',
                    type='number',
                    placeholder="Enter threshold value",
                    style={"width": "100%"}
                ),
            ], style={"width": "30%", "marginRight": "10px"}),

            html.Div([
                html.Label("Condition:"),
                dcc.RadioItems(
                    id='threshold-condition',
                    options=[
                        {'label': 'Above', 'value': 'above'},
                        {'label': 'Below', 'value': 'below'},
                    ],
                    value='above',
                    style={"marginTop": "5px"}
                ),
            ], style={"width": "30%"}),
        ], style={"display": "flex", "alignItems": "center", "marginBottom": "0px"}),

        html.Div([
            html.Div([
                html.P("Data Points:"),
                html.P(id='data-points', style={"border":"5px solid #ccc","padding":"5px","borderRadius":"5px","display": "inline-block","minwidth": "50px", "textAlign": "center"})
            ],style={"width": "25%", "textAlign": "center"}),
            html.Div([
                html.P("Minimum:"),
                html.P(id='min-value',style={"border":"5px solid #ccc","padding":"5px","borderRadius":"5px","display": "inline-block","minwidth": "50px", "textAlign": "center"})
            ], style={"width": "25%", "textAlign": "center"}),
            html.Div([
                html.P("Maximum:"),
                html.P(id='max-value',style={"border":"5px solid #ccc","padding":"5px","borderRadius":"5px","display": "inline-block","minwidth": "50px", "textAlign": "center"})
            ], style={"width": "25%", "textAlign": "center"}),
            html.Div([
                html.P("Average:"),
                html.P(id='avg-value',style={"border":"5px solid #ccc","padding":"5px","borderRadius":"5px","display": "inline-block","minwidth": "50px", "textAlign": "center"})
            ], style={"width": "25%", "textAlign": "center"})
        ], style={"display": "flex","justifyContent": "space-around", "marginTop": "0px"}),
        dcc.Graph(id='time-series-chart')
    ])