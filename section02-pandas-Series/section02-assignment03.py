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
    # Assignment 3: Sorting and Filtering Series

    * First, get the 10 lowest prices from the data.
    * Sort the 10 lowest prices by date, starting with the most recent and ending with the oldest price.

    * Finally, use the list of provided dates. Select only rows with these dates that had a price of less than 50 dollars per barrel.
    """)
    return


@app.cell
def _():
    # list of dates to be used to solve bullet 3

    dates = [
        "2016-12-22",
        "2017-05-03",
        "2017-01-06",
        "2017-03-05",
        "2017-02-12",
        "2017-03-21",
        "2017-04-14",
        "2017-04-15",
    ]
    return (dates,)


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
    return (oil_series,)


@app.cell
def _(oil_series):
    ten_lowest_prices = oil_series.sort_values(ascending=True).iloc[:10]

    print(ten_lowest_prices.size)
    print(ten_lowest_prices)
    return (ten_lowest_prices,)


@app.cell
def _(ten_lowest_prices):
    ten_lowest_prices_sort_by_date = ten_lowest_prices.sort_index(ascending=False)
    print(ten_lowest_prices_sort_by_date.size)
    print(ten_lowest_prices_sort_by_date)
    return


@app.cell
def _(dates, oil_series):
    date_filtered_indexes = oil_series.index.isin(dates)

    print(date_filtered_indexes)
    return (date_filtered_indexes,)


@app.cell
def _(oil_series):
    value_filter = oil_series < 50

    print(value_filter)
    return (value_filter,)


@app.cell
def _(date_filtered_indexes, oil_series, value_filter):
    date_and_value_filtered_prices = oil_series.loc[
        date_filtered_indexes & value_filter
    ]

    print(date_and_value_filtered_prices.size)
    print(date_and_value_filtered_prices)
    return


if __name__ == "__main__":
    app.run()
