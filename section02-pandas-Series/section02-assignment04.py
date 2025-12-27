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
    # Assignment 4: Series Operations

    * Increase the prices in the oil series by 10%, and add an additional 2 dollars per barrel on top of that.

    * Then, create a series that represents the difference between each price and max price.

    * Finally, extract the month from the string dates in the index and store them as an integer in their own series.
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
def _(oil_series):
    increased_prices = oil_series * 1.1 + 2
    print(increased_prices)
    return (increased_prices,)


@app.cell
def _(increased_prices):
    max_price = increased_prices.max()
    print(max_price)
    return (max_price,)


@app.cell
def _(increased_prices, max_price):
    percentual_diff_from_max = increased_prices / max_price - 1

    print(percentual_diff_from_max)
    return


@app.cell
def _(increased_prices, pd):
    months = (
        pd.Series(increased_prices.index)
        .str.split("-", expand=True)
        .iloc[:, 1]
        .astype("int")
    )

    print(type(months))
    print(months)
    return


if __name__ == "__main__":
    app.run()
