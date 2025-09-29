from users import products

def get_products_in_price_range(products: list[dict], min_price: float, max_price: float) -> list[dict]:
    res = []
    for p in products:
        if p["price"] >= min_price and p["price"] <= max_price:
            res.append(p)
    
    return res

print(get_products_in_price_range(products, 300, 1000))