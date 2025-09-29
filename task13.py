from users import products

def get_unique_categories(products: list[dict]) -> list[str]:
    categories = set()
    for product in products:
        categories.add(product["category"])
    
    return list(categories)

print(get_unique_categories(products))
