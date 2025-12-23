import marimo

__generated_with = "0.18.4"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Assignment 7: Bringing it All Together

    Ok, final NumPy task - let's read in some data with the help of Pandas.

    Our data scientist provided the code to read in a csv as a Pandas dataframe, and has converted the two columns of interest to arrays.

    * Filter `sales_array` down to only sales where the product family was produce.

    * Then, randomly sample roughly half (random number < .5) of the produce sales and report the mean and median sales. Use a random seed of 2022.

    * Finally, create a new array that has the values 'above_both', 'above_median', and 'below_both' based on whether the sales were above the median and mean of the sample, just above the median of the sample, or below both the median and mean of the sample.
    """)
    return


@app.cell
def _(mo):
    import os
    from pathlib import Path

    import numpy as np
    import pandas as pd

    notebook_path = mo.notebook_location()
    parent_path = Path(notebook_path).parent

    csv_file_path = os.path.join(
        parent_path, "Pandas Course Resources", "retail", "retail_2016_2017.csv"
    )

    # print(csv_file_path)

    retail_df = pd.read_csv(csv_file_path, skiprows=range(1, 11000), nrows=1000)

    family_array = np.array(retail_df["family"])
    _ = family_array
    sales_array = np.array(retail_df["sales"])
    _ = sales_array
    return


if __name__ == "__main__":
    app.run()
