"""
Solution to assignment 06 of Section 01

Assignment 6: Aggregating and Sorting Arrays
First, grab the top 3 highest priced items in our list.
Then, calculated the mean, min, max, and median of the top three prices.
Finally, calculate the number of unique price tiers in our `price_tiers` array.
"""

from typing import Any

import numpy as np


def main() -> None:
    products: np.ndarray[tuple[Any, ...], np.dtype[Any]] = np.array(
        object=["salad", "bread", "mustard", "rare tomato", "cola", "gourmet ice cream"]
    )
    print(f"Products: {products}")

    prices: np.ndarray[tuple[Any, ...], np.dtype[Any]] = np.array(
        object=[5.99, 6.99, 22.49, 99.99, 4.99, 49.99]
    )
    print(f"Prices: {prices}")

    indexes = np.linspace(start=0, stop=products.size - 1, num=products.size)
    print(f"Indexes: {indexes}")

    prices_asc: np.ndarray[tuple[Any, ...], np.dtype[Any]] = np.sort(a=prices)
    prices_desc: np.ndarray[tuple[Any, ...], np.dtype[Any]] = prices_asc[::-1]

    print(f"Prices in ascending order: {prices_asc}")
    print(f"Prices in descending order: {prices_desc}")

    top1_price_mask = prices == prices_desc[0]
    top2_price_mask = prices == prices_desc[1]
    top3_price_mask = prices == prices_desc[2]
    price_mask = top1_price_mask | top2_price_mask | top3_price_mask

    top3_priced_products_not_sorted = products[price_mask]
    top3_indexes = indexes[price_mask]

    print(top3_priced_products_not_sorted)
    print(top3_indexes)

    top_3_prices = np.where(price_mask, prices, 0)
    top_3_prices = top_3_prices[top_3_prices > 0]

    print(f"Mean price of top 3 prices: $ {top_3_prices.mean()}")
    print(f"Max price of top 3 prices: $ {top_3_prices.max()}")
    print(f"Min price of top 3 prices: $ {top_3_prices.min()}")
    print(f"Median price of top 3 prices: $ {np.median(a=top_3_prices)}")

    price_tiers = np.array(
        ["budget", "budget", "mid-tier", "luxury", "mid-tier", "luxury"]
    )
    print(f"Unique price tiers: {np.unique(price_tiers)}")


if __name__ == "__main__":
    main()
