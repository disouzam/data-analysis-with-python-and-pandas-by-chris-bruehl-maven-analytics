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
    # Assignment 2:  Accessing Series Data

    * Set the date series, which has been created below, to be the index of the oil price series created in assignment 1.


    * Then, take the mean of the first 10 and last 10 prices of the series.


    * Finally, grab all oil prices from January 1st, 2017 - January 7th, 2017 (inclusive) and set the index to the default integer index.
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
    return oil, oil_series


@app.cell
def _(oil, pd):
    # extract date column from oil DataFrame and grab first 100 rows

    dates = pd.Series(oil["date"]).iloc[1000:1100]
    return (dates,)


@app.cell
def _(oil_series):
    oil_series_2 = oil_series.reset_index(drop=True)
    print(oil_series_2)
    print(type(oil_series_2))
    return (oil_series_2,)


@app.cell
def _(dates, oil_series_2):
    oil_series_2.index = dates
    print(oil_series_2)
    return


@app.cell
def _(oil_series_2):
    print(oil_series_2.index)
    return


@app.cell
def _(oil_series_2):
    first_10_prices = oil_series_2.iloc[:10]
    print(first_10_prices)
    print(first_10_prices.size)

    _mean = first_10_prices.mean()

    print(f"Mean of first 10 prices: {_mean:.2f}")
    return


@app.cell
def _(oil_series_2):
    last_10_prices = oil_series_2.iloc[-10:]
    print(last_10_prices)
    print(last_10_prices.size)

    _mean = last_10_prices.mean()

    print(f"Mean of last 10 prices: {_mean:.2f}")
    return


@app.cell
def _(oil_series_2):
    oil_series_3 = oil_series_2.reset_index(drop=True)
    print(oil_series_3)
    return


if __name__ == "__main__":
    app.run()
