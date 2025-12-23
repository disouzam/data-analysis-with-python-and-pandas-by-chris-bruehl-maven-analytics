import marimo

__generated_with = "0.18.4"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(prices, products):
    # Products with prices greater than 25
    over25_prices = products[prices > 25]
    print(over25_prices)
    return


@app.cell
def _(np, prices, products):
    # Products with prices greater than 25
    over25_prices_2 = np.where(prices > 25, products, "OVER_PRICED_25")
    print(over25_prices_2)
    return


@app.cell
def _(prices, products):
    price_mask = prices > 25
    print(f"Price mask: {price_mask}")

    product_mask = products == "cola"
    print(f"Product mask: {product_mask}")

    fancy_feast_special = products[price_mask | product_mask]
    fancy_feast_special_2 = products[(prices > 25) | (products == "cola")]

    print(f"Fancy feast special 1: {fancy_feast_special}")
    print(f"Fancy feast special 2: {fancy_feast_special_2}")

    return


@app.cell
def _(np, prices):
    shipping_cost_array = np.where(prices > 20, 0, 5)
    print(shipping_cost_array)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Using masks
    """)
    return


@app.cell
def _(np, prices):
    shipping_cost_mask = prices <= 20
    print(shipping_cost_mask)

    shipping_cost_array_2 = np.zeros(6)
    shipping_cost_array_2[shipping_cost_mask] = 5
    print(shipping_cost_array_2)
    return


@app.cell
def _():
    import numpy as np

    return (np,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Assignment 5: Filtering Arrays

    Filter the product array to only include those with prices greater than 25.

    Modify your logic to include cola, despite it not having a price greater than 25.
    Store the elements returned in an array called `fancy_feast_special`.

    Next, create a shipping cost array where the cost is 0 if price is greater than 20, and 5 if not.
    """)
    return


@app.cell
def _(np):
    prices = np.array([5.99, 6.99, 22.49, 99.99, 4.99, 49.99])
    products = np.array(
        ["salad", "bread", "mustard", "rare tomato", "cola", "gourmet ice cream"]
    )

    print(products)
    print(prices)
    zipped_list = list(zip(products, prices))

    print()

    for item in zipped_list:
        print(item)
    return prices, products


if __name__ == "__main__":
    app.run()
