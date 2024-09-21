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
        'D': 15
    }

    # Special offers
    offers = {
        'A': (3, 130), # 3 A's for 130
        'B': (2, 45)   # 2 B's for 45
    }

    # Count occurrences of each SKU
    counts = {}
    for sku in skus:
        if sku not in prices:
            return -1  # Invalid SKU
        counts[sku] = counts.get(sku, 0) + 1

    # Calculate total price
    total = 0
    for sku, count in counts.items():
        if sku in offers:
            offer_count, offer_price = offers[sku]
            total += (count // offer_count) * offer_price  # Apply special offer
            total += (count % offer_count) * prices[sku]  # Apply remaining items
        else:
            


