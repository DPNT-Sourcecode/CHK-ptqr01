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
        'A': 50, 'B': 30, 'C': 20, 'D': 15, 'E': 40, 'F': 10,
        'G': 20, 'H': 10, 'I': 35, 'J': 60, 'K': 70, 'L': 90,
        'M': 15, 'N': 40, 'O': 10, 'P': 50, 'Q': 30, 'R': 50,
        'S': 20, 'T': 20, 'U': 40, 'V': 50, 'W': 20, 'X': 17,
        'Y': 20, 'Z': 21
    }

    # Offers table (tuple: (quantity, price))
    offers = {
        'A': [(5, 200), (3, 130)],
        'B': [(2, 45)],
        'E': [(2, 'B')],  # Buy 2 E's, get 1 B for free
        'F': [(3, 20)],  # Buy 2 F's, get 1 F for free
        'H': [(10, 80), (5, 45)],
        'K': [(2, 120)],
        'N': [(3, 'M')],  # Buy 3 N's, get 1 M for free
        'P': [(5, 200)],
        'Q': [(3, 80)],
        'R': [(3, 'Q')],  # Buy 3 R's, get 1 Q for free
        'U': [(4, 120)],  # Buy 3 U's, get 1 U for free
        'V': [(3, 130), (2, 90)]
    }

    # Items for the group discount (buy any 3 for 45)
    group_discount_items = ['S', 'T', 'X', 'Y', 'Z']

    # Count occurrences of each SKU
    counts = {}
    for sku in skus:
        if sku not in prices:
            return -1  # Invalid SKU
        counts[sku] = counts.get(sku, 0) + 1

    # Calculate total price
    total = 0

    # Step 1: Apply free item offers first
    for sku, offer_list in offers.items():
        if sku in counts:  # Only apply offers for items that are in the basket
            for offer in offer_list:
                if isinstance(offer[1], str):
                    free_sku = offer[1]
                    # Check if the free item exists in the basket
                    if free_sku in counts:
                        # Apply "get 1 free" type offers (e.g. buy 2 E's -> get 1 B free)
                        free_item_count = (counts[sku] // offer[0])
                        counts[offer[1]] = max(0, counts[free_sku] - free_item_count)

    # Step 2: Apply discounts and compute the total
    for sku, count in counts.items():
        if sku in offers:
            for offer in offers[sku]:
                if isinstance(offer[1], int):
                    total += (count // offer[0]) * offer[1]  # Apply the offer
                    count %= offer[0]  # Remaining items after applying the offer

        # Apply the remaining full-price items
        total += count * prices[sku]

    # Step 3: Apply group discount
    group_discount_count = sum(counts.get(sku, 0) for sku in group_discount_items)
    group_discount_sets = group_discount_count // 3
    total -= group_discount_sets * sum(prices[sku] for sku in group_discount_items[:group_discount_sets * 3])
    total += group_discount_sets * 45

    return total

