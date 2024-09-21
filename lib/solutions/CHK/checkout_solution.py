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

    # Apply special offers for A (favoring the customer with best deal)
    if 'A' in counts:
        count_a = counts['A']
        total += (count_a // 5) * 200  # Apply 5 A's offer
        count_a %= 5
        total += (count_a // 3) * 130  # Apply 3 A's offer
        count_a %= 3
        total += count_a * prices['A']  # Apply remaining A's

    # Apply special offers for B
    if 'B' in counts:
        count_b = counts['B']
        if 'E' in counts:
            count_e = counts['E']
            free_b_count = count_e // 2   # One B free for every two E's
            count_b = max(0, count_b - free_b_count)  # Deduct free B's
        total += (count_b // 2) * 45   # Apply 2 B's offer
        total += (count_b % 2) * prices['B'] # Apply remaining B's

    # Apply special offers for E
    if 'E' in counts:
        total += counts['E'] * prices['E']

    # Apply prices for items w/o special offers
    for sku in ['C', 'D']:
        if sku in offers:
            print(">>> sku: ", sku)
            total += counts[sku] * prices[sku]

    return total






