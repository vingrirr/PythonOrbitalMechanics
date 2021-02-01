import plotly.express as px
import pandas as pd


class PlotTest():
   
    def plot_polar():
        df = px.data.wind()
        fig = px.line_polar(df, r="frequency", theta="direction", color="strength", line_close=True,
                            color_discrete_sequence=px.colors.sequential.Plasma_r,
                            template="plotly_dark",)
        fig.show()


