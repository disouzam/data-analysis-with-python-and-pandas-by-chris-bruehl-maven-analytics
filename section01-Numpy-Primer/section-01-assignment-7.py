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
    sales_array = np.array(retail_df["sales"])
    return family_array, np, sales_array


@app.cell
def _(family_array, sales_array):
    print(f"Shape of family_array: {family_array.shape}")
    print(f"Shape of sales_array: {sales_array.shape}")
    return


@app.cell
def _(family_array, sales_array):
    print(f"First 5 items in family_array: {family_array[:5]}...")
    print(f"First 5 items in sales_array: {sales_array[:5]}...")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Filtering sales array
    """)
    return


@app.cell
def _(family_array, np, sales_array):
    indexes = np.linspace(0, family_array.size - 1, family_array.size)
    print(f"- First/ last 5 items in indexes: {indexes[:5]}...{indexes[-5:]}")

    produce_product_family_mask = family_array == "PRODUCE"
    filtered_family_array = family_array[produce_product_family_mask]

    print(f"- Number of items in filtered_family_array: {filtered_family_array.size}")
    print(
        f"- First/ last 5 items in filtered_family_array: {filtered_family_array[:5]}...{filtered_family_array[-5:]}"
    )

    filtered_indexes = indexes[produce_product_family_mask]

    print(
        f"- First/ last 5 items in filtered indexes: {filtered_indexes[:5]}...{filtered_indexes[-5:]}"
    )

    filtered_sales = sales_array[produce_product_family_mask]
    print(
        f"- First/ last 5 items in filtered sales array: {filtered_sales[:5]}...{filtered_sales[-5:]}"
    )
    return (filtered_sales,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Random sampling
    """)
    return


@app.cell
def _(filtered_sales, np):
    rng = np.random.default_rng(2022)
    random_array = rng.random(30)
    print(
        f"- First/ last 5 items in random generated array: {random_array[:5]}...{random_array[-5:]}"
    )

    random_mask = random_array < 0.5
    print(
        f"- First/ last 5 items in random mask: {random_mask[:5]}...{random_mask[-5:]}"
    )

    random_sales = filtered_sales[random_mask]
    print()
    print(f"- Size of random sales: {random_sales.size}")
    print(
        f"- First/ last 5 items in random sales: {random_sales[:5]}...{random_sales[-5:]}"
    )
    return (random_sales,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Mean and median sales
    """)
    return


@app.cell
def _(np, random_sales):
    mean_sales = random_sales.mean()
    median_sales = np.median(random_sales)

    print(f"- Median sales: {median_sales.round(2)}")
    print(f"- Mean sales: {mean_sales.round(2)}")
    return mean_sales, median_sales


@app.cell
def _(mean_sales, median_sales, random_sales):
    above_mean_mask = random_sales > mean_sales
    below_median_mask = random_sales < median_sales
    above_median_mask = (random_sales >= median_sales) & (random_sales <= mean_sales)
    return above_mean_mask, above_median_mask, below_median_mask


@app.cell
def _(above_mean_mask, above_median_mask, below_median_mask, np, random_sales):
    result_array = np.array(["EMPTY"] * random_sales.size, dtype="<U12")

    print(result_array.dtype)

    result_array[above_mean_mask] = "above_both"
    result_array[below_median_mask] = "below_both"
    result_array[above_median_mask] = "above_median"

    check_result_mask = result_array == "EMPTY"
    check_result_array = result_array[check_result_mask]
    print(check_result_array.size)
    assert check_result_array.size == 0, (
        "EMPTY is default value that should be replaced"
    )

    print(result_array)
    return


if __name__ == "__main__":
    app.run()
