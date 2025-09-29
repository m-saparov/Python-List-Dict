from users import products

def get_most_expensive_product(products: list[dict]) -> dict:
    exp_product = products[0]

    for product in products:
        if product["price"] > exp_product["price"]:
            exp_product = product
    
    return exp_product

print(get_most_expensive_product(products))

