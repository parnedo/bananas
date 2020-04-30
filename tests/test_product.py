import unittest
import sys
sys.path.insert(0, '.')

from product import Product


class TestProduct(unittest.TestCase):
    def test_get_contains_ingredient__invalid_ingredient(self):
        with self.assertRaises(Exception) as context:
            Product.search_contains_ingredient("banana")
            self.assertTrue("invalid input, expecting int received <class 'str'> (banana)" in str(context.exception))


    def test_get_contains_ingredient__missing_ingredient(self):
        self.assertEqual(Product.search_contains_ingredient(0), [])

    def test_get_contains_ingredient__organic_banana(self):
        products = Product.search_contains_ingredient(3)
        self.assertEqual(products[0].id, 1)
        self.assertEqual(products[0].name, "Acai + Cherry")
        self.assertEqual(products[0].collection, "smoothie")
        self.assertEqual(products[0].ingredient_ids, [1, 2, 3, 4, 5])

        self.assertEqual(products[1].id, 2)
        self.assertEqual(products[1].name, "Chocolate + Blueberry")
        self.assertEqual(products[1].collection, "smoothie")
        self.assertEqual(products[1].ingredient_ids, [3, 4, 5, 12, 26])

        self.assertEqual(products[2].id, 4)
        self.assertEqual(products[2].name, "Cinnamon + Banana")
        self.assertEqual(products[2].collection, "oat bowl")
        self.assertEqual(products[2].ingredient_ids, [3, 19, 20, 21, 22, 26])

        self.assertEqual(products[3].id, 6)
        self.assertEqual(products[3].name, "Ginger + Greens")
        self.assertEqual(products[3].collection, "smoothie")
        self.assertEqual(products[3].ingredient_ids, [3, 7, 10, 11, 12])

    def test_to_json(self):
        p = Product(1, "Mousse au chocolat", "Dessert", [7, 13, 45])
        self.assertEqual(p.to_dict(), {'id': 1, 'name': 'Mousse au chocolat', 'collection': 'Dessert', 'ingredient_ids': [7, 13, 45]})


if __name__ == '__main__':
    unittest.main()
