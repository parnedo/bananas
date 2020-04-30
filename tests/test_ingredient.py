import unittest
import sys
sys.path.insert(0, '.')

from ingredient import Ingredient


class TestIngredient(unittest.TestCase):
    def test_missing_ingredient(self):
        self.assertEqual(Ingredient.retrieve_by_name("Missing Ingredient"), None)

    def test_organic_banana(self):
        banana = Ingredient.retrieve_by_name("Organic Banana")
        self.assertEqual(banana.id, 3)
        self.assertEqual(banana.name, "Organic Banana")
        self.assertFalse(banana.is_allergen)


if __name__ == '__main__':
    unittest.main()
