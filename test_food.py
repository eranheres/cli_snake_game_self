import unittest
from cli_snake_game.food import Food

class TestFood(unittest.TestCase):
    def test_init(self):
        food = Food()
        self.assertEqual(food.position, (100, 100))

    def test_generate(self):
        food = Food()
        initial_position = food.position
        food.generate()
        self.assertNotEqual(food.position, initial_position)

if __name__ == '__main__':
    unittest.main()
