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
    # Assignment 1: Series Basics

    The code has been provided to create an array, `oil_array` from a dataframe column.

    * Convert `oil_array` into a Pandas Series, called `oil_series`. Give it a name!
    * Return the name, dtype, size, and index of `oil_series`.

    Take the mean of the values array.

    Then, convert the series to integer datatype and recalculate the mean.
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

    oil_array
    return (oil_array,)


@app.cell
def _(oil_array, pd):
    oil_series = pd.Series(oil_array, name="prices of oil")
    print(oil_series)
    return (oil_series,)


@app.cell
def _(oil_series):
    print(oil_series.name)
    print(oil_series.dtype)
    print(oil_series.size)
    print(oil_series.index)
    return


@app.cell
def _(oil_series):
    # Calculate mean value of oil series
    print(f"{oil_series.mean():.2f}")
    return


@app.cell
def _(oil_series):
    # Cast values to int
    oil_series_2 = oil_series.astype(int)

    # Calculate mean value of int-converted values
    print(f"{oil_series_2.mean():.2f}")
    return (oil_series_2,)


@app.cell
def _(oil_series_2):
    print(oil_series_2)
    return


if __name__ == "__main__":
    app.run()
