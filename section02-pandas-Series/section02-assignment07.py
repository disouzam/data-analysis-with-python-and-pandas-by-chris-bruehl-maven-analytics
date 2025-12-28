import marimo

__generated_with = "0.18.4"
app = marimo.App(width="full")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Exercise 7: Apply and Where

    Write a function that outputs ‘buy’ if price is less than the 90th percentile and ‘wait’ if it’s not. Apply it to the oil series.

    Then, create a series that multiplies price by .9 if the date is ‘2016-12-23’ or ‘2017-05-10’, and 1.1 for all other dates.
    """)
    return


@app.cell
def _():
    # import libraries needed
    import os
    from pathlib import Path

    import numpy as np
    import pandas as pd

    return Path, np, os, pd


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
    percentiles = oil_series.quantile([0.10, 0.25, 0.50, 0.75, 0.90])
    print(percentiles)

    percentile_50th = percentiles.loc[0.5]
    print(percentile_50th)

    percentile_90th = percentiles.loc[0.9]
    print(percentile_90th)
    return (percentile_90th,)


@app.function
def stock_decision(price, threshold):
    if price < threshold:
        return "buy"
    else:
        return "wait"


@app.cell
def _(oil_series, percentile_90th):
    stock_results = oil_series.apply(stock_decision, args=[percentile_90th])

    print(stock_results)
    return


@app.cell
def _(oil_series):
    adjusted_oil_series = oil_series.where(
        oil_series.index.isin(["2016-12-23", "2017-05-10"]), oil_series * 1.1
    ).where(~oil_series.index.isin(["2016-12-23", "2017-05-10"]), oil_series * 0.9)

    print(adjusted_oil_series - oil_series)
    return


if __name__ == "__main__":
    app.run()
