from users import products

def get_all_product_prices(products: list[dict]) -> list[float]:
    prices = []
    for product in products:
        prices.append(float(product["price"]))
    
    return prices


print(get_all_product_prices(products))