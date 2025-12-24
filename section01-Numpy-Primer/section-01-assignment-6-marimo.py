import marimo

__generated_with = "0.18.4"
app = marimo.App(width="medium")


@app.cell
def _():
    import numpy as np

    return (np,)


@app.cell
def _(np):
    products = np.array(
        object=["salad", "bread", "mustard", "rare tomato", "cola", "gourmet ice cream"]
    )
    print(f"Products: {products}")
    return (products,)


@app.cell
def _(np):
    prices = np.array(object=[5.99, 6.99, 22.49, 99.99, 4.99, 49.99])
    print(f"Prices: {prices}")
    return (prices,)


@app.cell
def _(np, products):
    indexes = np.linspace(start=0, stop=products.size - 1, num=products.size)
    print(f"Indexes: {indexes}")
    return (indexes,)


@app.cell
def _(np, prices):
    prices_asc = np.sort(a=prices)
    prices_desc = prices_asc[::-1]

    print(f"Prices in ascending order: {prices_asc}")
    print(f"Prices in descending order: {prices_desc}")
    return (prices_desc,)


@app.cell
def _(indexes, prices, prices_desc, products):
    top1_price_mask = prices == prices_desc[0]
    top2_price_mask = prices == prices_desc[1]
    top3_price_mask = prices == prices_desc[2]
    price_mask = top1_price_mask | top2_price_mask | top3_price_mask

    top3_priced_products_not_sorted = products[price_mask]
    top3_indexes = indexes[price_mask]

    print(top3_priced_products_not_sorted)
    print(top3_indexes)
    return (price_mask,)


@app.cell
def _(np, price_mask, prices):
    top_3_prices = np.where(price_mask, prices, 0)
    top_3_prices = top_3_prices[top_3_prices > 0]
    top_3_prices

    print(f"Mean price of top 3 prices: $ {top_3_prices.mean()}")
    print(f"Max price of top 3 prices: $ {top_3_prices.max()}")
    print(f"Min price of top 3 prices: $ {top_3_prices.min()}")
    print(f"Median price of top 3 prices: $ {np.median(a=top_3_prices)}")
    return


@app.cell
def _(np):
    price_tiers = np.array(
        ["budget", "budget", "mid-tier", "luxury", "mid-tier", "luxury"]
    )
    print(f"Unique price tiers: {np.unique(price_tiers)}")
    return


if __name__ == "__main__":
    app.run()
