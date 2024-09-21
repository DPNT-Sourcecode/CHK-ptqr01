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
        'G': 20, 'H': 10, 'I': 35, 'J': 60, 'K': 80, 'L': 90,
        'M': 15, 'N': 40, 'O': 10, 'P': 50, 'Q': 30, 'R': 50,
        'S': 30, 'T': 20, 'U': 40, 'V': 50, 'W': 20, 'X': 90,
        'Y': 10, 'Z': 50
    }

    # Offers table (tuple: (quantity, price))
    offers = {
        'A': [(5, 200), (3, 130)],
        'B': [(2, 45)],
        'E': [(2, 'B')],  # Buy 2 E's, get 1 B for free
        'F': [(3, 20)],  # Buy 2 F's, get 1 F for free
        'H': [(10, 80), (5, 45)],
        'K': [(2, 150)],
        'P': [(5, 200)],
        'Q': [(3, 80)],
        'R': [(3, 'Q')],  # Buy 3 R's, get 1 Q for free
        'U': [(4, 120)],  # Buy 3 U's, get 1 U for free
        'V': [(3, 130), (2, 90)]
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

    # Apply special offers for F
    if 'F' in counts:
        count_f = counts['F']
        total += (count_f // 3) * 20  # Apply "buy 2, get 1 free" offer (3 F's for 20)
        total += (count_f % 3) * prices['F'] # Apply remaining F's

    # Apply prices for items w/o special offers
    for sku in ['C', 'D']:
        if sku in counts:
            total += counts[sku] * prices[sku]

    return total



