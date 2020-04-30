import json
from typing import TypeVar


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

