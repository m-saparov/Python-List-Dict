from users import products

def get_products_above_price(products: list[dict], price: float) -> list[dict]:
    result = []

    for product in products:
        if product["price"] > price:
            result.append(product)

    return result

print(get_products_above_price(products, 1000))