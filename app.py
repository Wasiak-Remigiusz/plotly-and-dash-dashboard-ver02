# import imp
from gc import callbacks
from ntpath import join
from subprocess import call
from typing import List

import dash_bootstrap_components as dbc
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from dash import Dash, Input, Output, dcc, html

from components.filtering import data_year_slider

# Import from packages from the application
from components.static import navbar
from data.external import data_gapminder_df
from graphs.templates import (
    bar_country,
    choropleth_world,
    line_country,
    scatter_gdpPercap,
)

# Creating a Dash App
app = Dash(__name__, external_stylesheets=["/assets/css/style.css",
                                            "https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700&display=swap",
                                            dbc.themes.CYBORG])


# Layout
app.layout = navbar,dbc.Container(
    fluid=True,
    children=
    [
        # navbar,
        html.Br(),
        dbc.Row(
            [
                dbc.Col(html.H5("Display year: "), xs=12, sm=4, md=3, lg=2),
                dbc.Col(data_year_slider(), xs=12, sm=8, md=9, lg=10),
            ],
            justify="center",
            className="custom-row-container"
        ),
        dbc.Row(
            [
                dbc.Col(
                    id="choropleth-world-col", children=choropleth_world(), xs=12, lg=6, className="equal-height"
                ),
                dbc.Col(
                    id="scatter-gdpPercap-col",
                    children=scatter_gdpPercap(),
                    xs=12, lg=6,className="equal-height"
                ),
            ],className="row-flex", 
            justify="center",
        ),
        dbc.Row(
            [
                dbc.Col(html.H5(id="outpout_cointener", children=[]), xs=3, sm=3, md=3, lg=3),
            ],
            justify="center",
            className="custom-row-container"
        ),
        dbc.Row(
            [
                dbc.Col(id="line-country-col", children=line_country(),  xs=12, lg=6),
                dbc.Col(id="bar-country-col", children=bar_country(),  xs=12, lg=6),
            ],
            justify="center",
        ),
    ],
)

# Callback for top charts (1, 2)
@app.callback(
    Output("choropleth-world-col", "children"),
    Output("scatter-gdpPercap-col", "children"),
    Input("data-year-slider", "value"),
)
def update_graphs(selected_year: List[float]):

    return (choropleth_world(selected_year), scatter_gdpPercap(selected_year))


# Callback for charts from below (3, 4)
@app.callback(
    Output("line-country-col", component_property="children"),
    Output("bar-country-col", component_property="children"),
    Output("outpout_cointener", component_property="children"),
    Input("choropleth-world", component_property="clickData"),
    prevent_initial_call=True,
)
def update_graphs_3_and_4(clickData: dict):
    if clickData is not None:
        country_selected = clickData["points"][0]["hovertext"]
    else:
        country_selected = "click on the map above"
    container = "Displayed country: {}".format(country_selected)

    return (line_country(clickData), bar_country(clickData), container)


# Added for Render.com - Gunicorn
server = app.server
if __name__ == "__main__":
    # app.run_server(port=8062, debug=True)
    app.run(port=8062, debug=True)
    
