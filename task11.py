from users import products

def get_all_product_names(products: list[dict]) -> list[str]:
    result = []
    for product in products:
        result.append(product["name"])

    return result

print(get_all_product_names(products))