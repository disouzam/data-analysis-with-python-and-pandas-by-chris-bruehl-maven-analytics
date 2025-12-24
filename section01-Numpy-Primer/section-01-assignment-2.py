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
    # Assignment 2: Array Creation

    Thanks for your help with the first piece - I'm starting to understand some of the key differences between base Python data types and NumPy arrays.

    Does NumPy have anything like the range() function from base Python?

    If so:
    * create the same array from assignment 1 using a NumPy function.
    * Make it 5 rows and 2 columns.
    * It's ok if the datatype is float or int.
    """)
    return


@app.cell
def _(np):
    array = np.arange(10, 101, 10)
    print(array)
    return (array,)


@app.cell
def _(array):
    array_2 = array.reshape(5, 2)
    print(array_2)
    return (array_2,)


@app.cell
def _(array_2):
    print(array_2.dtype)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Using linspace
    """)
    return


@app.cell
def _(np):
    array_lp = np.linspace(10, 100, 10).reshape((5, 2))
    print(array_lp)
    print(array_lp.dtype)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Setting dtype on array creation
    """)
    return


@app.cell
def _(np):
    array_3 = np.arange(10, 101, 10, dtype=np.float64)
    array_3 = array_3.reshape(5, 2)
    print(array_3)
    print(array_3.dtype)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Random number generation
    """)
    return


@app.cell
def _(np):
    rng = np.random.default_rng(2022)

    random_array = rng.random((3, 3))
    print(random_array)
    return


if __name__ == "__main__":
    app.run()
