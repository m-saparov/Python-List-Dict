from users import products

def get_cheapest_product(products: list[dict]) -> dict:
    cheap_product = products[0]
    for product in products:
        if product["price"] < cheap_product["price"]:
            cheap_product = product
    
    return cheap_product

print(get_cheapest_product(products))