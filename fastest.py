from typing import List
from ingredient import Ingredient
from product import Product

def get_products_with_banana() -> List[Product]:
    banana = Ingredient.retrieve_by_name('Organic Banana')
    if not banana:
        return []

    return Product.search_contains_ingredient(banana.id)


for i in get_products_with_banana():
    print (i)
