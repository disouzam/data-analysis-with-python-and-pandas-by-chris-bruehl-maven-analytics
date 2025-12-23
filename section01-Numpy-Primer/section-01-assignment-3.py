import marimo

__generated_with = "0.18.4"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _():
    import numpy as np

    return (np,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Assignment 3: Accessing Array Data


    Slice and index the `random_array` we created in the previous exercise. Perform the following:

    * Grab the first two 'rows' of the array
    * Grab the entire first column
    * Finally, grab the second selement of the third row.

    Thanks!
    """)
    return


@app.cell
def _(np):
    rng = np.random.default_rng(2022)

    random_array = rng.random((3, 3))
    print(random_array)
    return (random_array,)


@app.cell
def _(random_array):
    # Grab the first two 'rows' of the array
    first_two_rows = random_array[0:2, :]
    print(first_two_rows)
    return


@app.cell
def _(random_array):
    # Grab the entire first column
    first_column = random_array[:, 0]
    print(first_column)
    print(first_column.shape)
    print(type(first_column))
    return


@app.cell
def _(random_array):
    # Finally, grab the second element of the third row.
    second_element_third_row = random_array[2, 1]
    print(second_element_third_row)
    return


if __name__ == "__main__":
    app.run()
