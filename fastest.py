import json
from typing import TypeVar
from typing import List


Ingredient = TypeVar('Ingredient')


class Ingredient:
    def __init__(self, id: int, name: str, is_allergen: bool):
        self.id = id
        self.name = name
        self.is_allergen = is_allergen

    @staticmethod
    def retrieve_by_name(name: str) -> Ingredient:
        with open("ingredients.json", "r") as read_file:
            for ingredient in json.load(read_file)['ingredients']:
                if ingredient.get('name', None) == name:
                    return Ingredient(**ingredient)
        return None

Product = TypeVar('Product')


class Product:
    def __init__(self, id: int, name: str, collection: str, ingredient_ids: List[int]) -> Product:
        self.id = id
        self.name = name
        self.collection = collection
        self.ingredient_ids = ingredient_ids

    def __str__(self):
        return f'{self.name} with id {self.id} that belongs to collection {self.collection} and contains {str(self.ingredient_ids)}'

    @staticmethod
    def get_contains_ingredient(ingredient_id):
        product_list = []
        with open("products.json", "r") as read_file:
            for product in json.load(read_file)['products']:
                if ingredient_id in product['ingredient_ids']:
                    product_list.append(Product(**product))
        return product_list


def get_products_with_banana() -> List[Product]:
    banana = Ingredient.retrieve_by_name('Organic Banana')
    if not banana:
        return []

    return Product.get_contains_ingredient(banana.id)


for i in get_products_with_banana():
    print (i)
