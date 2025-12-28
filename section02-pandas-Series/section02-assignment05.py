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
    # Assignment 5: Series Aggregations

    * Calculate the sum and mean of prices in the month of March.

    * Next, calculate how many prices were recorded in January and February.

    * Then, calculate the 10th and 90th percentiles across all data.

    * Finally, how often did integer dollar value (e.g. 51, 52) occur in the data? Normalize this to a percentage.
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
    return dates_for_index, oil_series


@app.cell
def _(dates_for_index, oil_series, pd):
    months = (
        pd.Series(oil_series.index).str.split("-", expand=True).iloc[:, 1].astype("int")
    )

    march_entries = months == 3
    march_entries.name = "March boolean filter"
    march_entries.index = dates_for_index

    jan_and_feb_entries = (months == 1) | (months == 2)
    jan_and_feb_entries.name = "January / February boolean filter"
    jan_and_feb_entries.index = dates_for_index
    print(months)
    print(march_entries)
    print(jan_and_feb_entries)
    return jan_and_feb_entries, march_entries


@app.cell
def _(march_entries, oil_series):
    march_prices = oil_series.loc[march_entries]
    print(march_prices)

    print(f"\nSum of prices in March: {march_prices.sum():.2f}")
    print(f"\nMean of prices in March: {march_prices.mean():.2f}")
    return


@app.cell
def _(jan_and_feb_entries, oil_series):
    jan_feb_prices = oil_series.loc[jan_and_feb_entries]
    print(f"There were {jan_feb_prices.count()} prices in January and February.")
    return


@app.cell
def _(oil_series):
    quantiles = oil_series.quantile([0.1, 0.9])
    print(quantiles)

    print(
        f"\nThe 10th-percentile was {quantiles.iloc[0]} and 90th-percentile was {quantiles.iloc[1]}"
    )
    return


@app.cell
def _(oil_series):
    oil_series_integer = oil_series.astype("int")

    print(oil_series_integer)

    print(oil_series_integer.value_counts(normalize=True))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Proposed solution and expliciting potential issues with it
    """)
    return


@app.cell
def _(oil_series):
    oil_series[oil_series.index.str[6:7].isin(["1", "2"])].count()
    return


@app.cell
def _(dates_for_index, oil_series, pd):
    stripped_month_series = pd.Series(oil_series.index.str[6:7])
    stripped_month_series.index = dates_for_index
    stripped_month_series = stripped_month_series.astype("int")
    print(stripped_month_series)
    return (stripped_month_series,)


@app.cell
def _(stripped_month_series):
    values_as_one = stripped_month_series.loc[stripped_month_series == 1]
    print(dict(values_as_one))
    return


@app.cell
def _(stripped_month_series):
    values_as_two = stripped_month_series.loc[stripped_month_series == 2]
    print(dict(values_as_two))
    return


if __name__ == "__main__":
    app.run()
