from users import products

def get_products_below_price(products: list[dict], price: float) -> list[dict]:
    result = []
    for p in products:
        if p["price"] < price:
            result.append(p)

    return result

print(get_products_below_price(products, 500))
