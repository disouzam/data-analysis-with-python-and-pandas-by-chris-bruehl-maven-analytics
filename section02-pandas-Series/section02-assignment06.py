import marimo

__generated_with = "0.18.4"
app = marimo.App(width="full")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _():
    # import libraries needed
    import os
    from pathlib import Path

    import numpy as np
    import pandas as pd

    return Path, np, os, pd


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Assignment 6: Missing Data

    There were some erroneous prices in our data, so they were filled in with missing values.

    Can you confirm the number of missing values in the price column?

    Once you’ve done that, fill the prices in with the median of the oil price series.
    """)
    return


@app.cell
def _(Path, mo, np, os, pd):
    notebook_path = mo.notebook_location()
    parent_path = Path(notebook_path).parent

    csv_file_path = os.path.join(
        parent_path, "Pandas Course Resources", "retail", "oil.csv"
    )

    # create a DataFrame from the oil file, drop missing values
    oil = pd.read_csv(csv_file_path).dropna()

    # Grab 100 rows of oil prices
    oil_array = np.array(oil["dcoilwtico"].iloc[1000:1100])
    oil_series = pd.Series(oil_array, name="prices of oil")

    # extract date column from oil DataFrame and grab first 100 rows
    dates_for_index = pd.Series(oil["date"]).iloc[1000:1100]

    oil_series.index = dates_for_index

    print(oil_series)
    return (oil_series,)


@app.cell
def _(oil_series, pd):
    # Fill in two values with missing data
    oil_series_2 = oil_series.where(~oil_series.isin([51.44, 47.83]), pd.NA)
    print(oil_series_2)
    return (oil_series_2,)


@app.cell
def _(oil_series_2):
    number_of_missing_values = oil_series_2.isna().sum()
    print(f"There were {number_of_missing_values} missing values in oil series data.")
    return


@app.cell
def _(oil_series_2):
    # Filling missing prices
    oil_series_3 = oil_series_2.fillna(oil_series_2.mean())

    number_of_missing_values_2 = oil_series_3.isna().sum()
    print(f"There were {number_of_missing_values_2} missing values in oil series data.")
    return (oil_series_3,)


@app.cell
def _(oil_series_2, pd):
    indexes_of_missing_values = pd.Series(
        oil_series_2.loc[oil_series_2.isna()].index, name="Index of missing values"
    )

    print(indexes_of_missing_values)
    return (indexes_of_missing_values,)


@app.cell
def _(indexes_of_missing_values, oil_series_3):
    # Filled missing values
    filled_values = oil_series_3.loc[
        oil_series_3.index.isin(list(indexes_of_missing_values))
    ]

    print(filled_values)
    return


if __name__ == "__main__":
    app.run()
