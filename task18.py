from users import products

def group_products_by_category(products: list[dict]) -> dict[str, list[dict]]:
    res = dict()

    for p in products:
        category = p["category"]
        if category not in res:
            res[category] = []
        
        res[category].append(p)

    return res
    
print(group_products_by_category(products))
