# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> int:
    """
    Calculate the total checkout value for the given SKUs.

    Args:
        skus (str): A string containing SKUs of the products in the basket.

    Returns:
        int: The total checkout value of the items, or -1 for illegal input.
    """
    # Price table
    prices = {
        'A': 50,
        'B': 30,
        'C': 20,
        'D': 15,
        'E': 40
    }

    # Special offers
    offers = {
        'A': [(5, 200), (3, 130)], # 5 A's for 200, 3 A's for 130
        'B': (2, 45),              # 2 B's for 45
        'E': (2, 'B')              # Buy 2 E's, get 1 B for free
    }

    # Count occurrences of each SKU
    counts = {}
    for sku in skus:
        if sku not in prices:
            return -1  # Invalid SKU
        counts[sku] = counts.get(sku, 0) + 1

    # Calculate total price
    total = 0

    # APply special offers for A (favoring the customer with best deal)
    if 'A' in counts:




    for sku, count in counts.items():
        if sku in offers:
            offer_count, offer_price = offers[sku]
            total += (count // offer_count) * offer_price  # Apply special offer
            total += (count % offer_count) * prices[sku]  # Apply remaining items
        else:
            total += count * prices[sku]

    return total


