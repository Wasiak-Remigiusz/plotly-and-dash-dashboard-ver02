from typing import List

import plotly.express as px
from dash import dcc

from data.external import data_gapminder_df


# Function that creates a cartogram
def choropleth_world(selected_year: List[float] = None) -> dcc.Graph:
    df = data_gapminder_df()
    if selected_year is not None:
        df = df[data_gapminder_df().year == selected_year]
    else:
        df = df[data_gapminder_df().year == 1952]

    # print("selected year", selected_year)
    # print(type(selected_year))

    return dcc.Graph(
        clickData=None,
        config={"staticPlot": False},
        id="choropleth-world",
        figure=px.choropleth(
            # data_gapminder_df()[data_gapminder_df().year == 2007],
            df,
            locations="iso_alpha",
            color="lifeExp",
            hover_name="country",
            color_continuous_scale=px.colors.sequential.Plasma,
            template="plotly_dark",
            # width=1200,
            height=650,
            title="Life Expectancy",
            hover_data={
                "iso_alpha": False,
                "lifeExp": True,
                "pop": True,
                "gdpPercap": True,
            },
        ),
    )


# Function that creates a graph with the logarithm
def scatter_gdpPercap(selected_year: List[float] = None) -> dcc.Graph:
    df = data_gapminder_df()
    if selected_year is not None:
        df = df[data_gapminder_df().year == selected_year]
    else:
        df = df[data_gapminder_df().year == 1952]

    return dcc.Graph(
        id="scatter-gdpPercap",
        figure=px.scatter(
            # data_gapminder_df()[data_gapminder_df().year == 2007],
            # data_gapminder_df(),
            df,
            x="gdpPercap",
            y="lifeExp",
            size="pop",
            color="continent",
            hover_name="country",
            log_x=True,
            size_max=60,
            template="plotly_dark",
            # width=1200,
            height=650,
            category_orders={
                "continent": ["Africa", "Americas", "Asia", "Europe", "Oceania"]
            },
            title="Life Expectancy vs GDP Per Capita (USD) - (logarithmic scale)",
        ),
    )


# Function that creates a line graph that shows GDP per Capita
def line_country(clickData: dict = None) -> dcc.Graph:

    df = data_gapminder_df()
    # print(type(clickData), clickData)

    if clickData is not None:
        country_selected = clickData["points"][0]["hovertext"]
        # print(type(country_selected), country_selected)
        df = df[data_gapminder_df().country == country_selected]
    else:
        df = df[data_gapminder_df().country == None]

    return dcc.Graph(
        id="line-country",
        figure=px.line(
            df,
            x="year",
            y="gdpPercap",
            color="country",
            markers=True,
            template="plotly_dark",
            title="GDP per capita (USD)",
        ),
    )


# Function that creates a column chart that shows the population
def bar_country(clickData: dict = None) -> dcc.Graph:

    df = data_gapminder_df()
    # print(type(clickData), clickData)

    if clickData is not None:
        country_selected = clickData["points"][0]["hovertext"]
        # print(type(country_selected), country_selected)
        df = df[data_gapminder_df().country == country_selected]
    else:
        df = df[data_gapminder_df().country == None]

    return dcc.Graph(
        id="bar-country",
        figure=px.bar(
            df,
            x="year",
            y="pop",
            # markers=True,
            template="plotly_dark",
            color="country",
            title="Population",
        ),
    )
