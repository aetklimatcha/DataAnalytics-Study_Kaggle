import pandas as pd 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# 결측치 퍼센트 계산
def calculate_missing(df):
    missing_values = df.isnull().sum()
    missing_percentage = (missing_values / len(df)) * 100
    return pd.DataFrame({'missing_values': missing_values, 'percentage': missing_percentage})

# 인풋과 아웃풋 정의 제공
def plot_count_plot(df: pd.DataFrame, column_name: str) -> px.histogram:
    """
    Generate a count plot for a specified column in the DataFrame using Plotly.

    Parameters
    ----------
    df : pandas.DataFrame
        The DataFrame containing the data.
    column_name : str
        The name of the column for which to create the count plot.

    Returns
    -------
    plotly.graph_objs._figure.Figure
        The Plotly figure object representing the count plot.
    """
    fig = px.histogram(
        df,
        x=column_name,
        title=f"Count Plot of {column_name}",
        category_orders={column_name: df[column_name].value_counts().index},
    )
    return fig


def plot_histogram(df: pd.DataFrame, column_name: str) -> px.histogram:
    """
    Generate a histogram for a specified column in the DataFrame using Plotly.

    Parameters
    ----------
    df : pandas.DataFrame
        The DataFrame containing the data.
    column_name : str
        The name of the column for which to create the histogram.

    Returns
    -------
    plotly.graph_objs._figure.Figure
        The Plotly figure object representing the histogram.
    """
    fig = px.histogram(df, x=column_name, title=f"Histogram of {column_name}")
    return fig


def plot_dataframe(df: pd.DataFrame) -> None:
    """
    Generate and display count plots or histograms for all columns in the DataFrame.
    For numeric columns, generate histograms.
    For categorical columns, generate count plots.

    Parameters
    ----------
    df : pandas.DataFrame
        The DataFrame containing the data.

    Returns
    -------
    None
    """
    for column in df.columns:
        if pd.api.types.is_numeric_dtype(df[column]):
            fig = plot_histogram(df, column)
        elif pd.api.types.is_object_dtype(df[column]):
            fig = plot_count_plot(df, column)
        else:
            continue
        fig.show()
def plot_boxplot(df: pd.DataFrame, column_name: str) -> px.box:
    fig = px.box(df, y=column_name, title=f"Boxplot of {column_name}")
    return fig