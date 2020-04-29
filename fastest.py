import json

def get_products_with_banana():
    banana_id = None
    with open("ingredients.json", "r") as read_file:
        for product in json.load(read_file)['ingredients']:
            if product.get('name', None) == 'Organic Banana':
                banana_id = product.get('id', None)
                if not banana_id:
                    raise "Banana missing id"
    if not banana_id:
        raise "Missing banana"

    product_list = []
    with open("products.json", "r") as read_file:
        for product in json.load(read_file)['products']:
            if banana_id in product['ingredient_ids']:
                product_list.append(product)
    return product_list

for i in get_products_with_banana():
    print (i)



