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
    # Assignment 4: Arithmetic Operations
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The creativity of our marketing team knows no bounds!

    They've asked us to come up with a simple algorithm to provide a random discount to our list of prices below.

    Before we do that,

    * Add a 5 dollar shipping fee to each price. Call this array `total`.

    Once we have that, we want to use the random_array created in assignment 2 and apply them to the 6 prices.

    * Grab the first 6 numbers from `random_array`, reshape it to one dimension. Call this `discount_pct`.
    * Subtract `discount_pct` FROM 1, store this in `pct_owed`.
    * Multiply `pct_owed` by `total` to get the final amount owed.
    """)
    return


@app.cell
def _(np):
    rng = np.random.default_rng(2022)

    random_array = rng.random((3, 3))

    print(random_array)
    return (random_array,)


@app.cell
def _(np):
    prices = np.array([5.99, 6.99, 22.49, 99.99, 4.99, 49.99])
    print(prices)
    return (prices,)


@app.cell
def _(prices):
    prices_plus_shipping = prices + 5
    total = prices_plus_shipping
    print(total)
    return (total,)


@app.cell
def _(random_array):
    discount_pct = random_array.reshape((1, 9))[0][:6]
    print(discount_pct)
    return (discount_pct,)


@app.cell
def _(discount_pct, np):
    pct_owed = np.ones(6) - discount_pct
    pct_owed_2 = 1 - discount_pct
    print(pct_owed)
    print(pct_owed_2)
    return (pct_owed,)


@app.cell
def _(pct_owed, total):
    final_amount_owed = total * pct_owed
    print(final_amount_owed.round(2))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # One liner
    """)
    return


@app.cell
def _(prices, random_array):
    one_liner_result = (
        (prices + 5)
        * (
            1
            - random_array.reshape(
                9,
            )[:6]
        )
    ).round(2)

    print(one_liner_result)
    return


if __name__ == "__main__":
    app.run()
