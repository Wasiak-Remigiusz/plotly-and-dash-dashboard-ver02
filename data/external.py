import pandas as pd
import plotly.express as px


# Importing data from the Plotly library
def data_gapminder_df() -> pd.DataFrame:
    return px.data.gapminder().round(2)
