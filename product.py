import json
from typing import TypeVar
from typing import List

Product = TypeVar('Product')


class Product:
    def __init__(self, id: int, name: str, collection: str, ingredient_ids: List[int]) -> Product:
        self.id = id
        self.name = name
        self.collection = collection
        self.ingredient_ids = sorted(ingredient_ids)

    def __str__(self) -> str:
        return f'{self.name} with id {self.id} that belongs to collection {self.collection} and contains {str(self.ingredient_ids)}'

    def __lt__(self, other) -> bool:
        ''' By default order by id because two products could have the same name '''
        return self.id < other.id

    def to_dict(self):
        return  {
            'id': self.id,
            'name': self.name,
            'collection': self.collection,
            'ingredient_ids': self.ingredient_ids
        }

    @staticmethod
    def search_contains_ingredient(ingredient_id: int) -> List[Product]:
        '''
        Will search all the products that contain the given ingredient
        We check valid input only integers are allowed ( we allow negative values for the moment )
        They will be returned ordered by id
        '''
        if not isinstance(ingredient_id, int):
            raise Exception(f"invalid input, expecting int received {type(ingredient_id)} ({ingredient_id})")

        product_list = []
        with open("products.json", "r") as read_file:
            for product in json.load(read_file)['products']:
                if ingredient_id in product['ingredient_ids']:
                    product_list.append(Product(**product))
        return sorted(product_list)
