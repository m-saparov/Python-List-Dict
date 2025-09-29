from users import products

def get_average_price_per_category(products: list[dict]) -> dict[str, float]:
    totals = {}
    counts = {}

    for product in products:
        category = product["category"]
        price = product["price"]

        totals[category] = totals.get(category, 0) + price
        counts[category] = counts.get(category, 0) + 1

    averages = {
        category: round(totals[category] / counts[category], 2)
        for category in totals
    }

    return averages

print(get_average_price_per_category(products))