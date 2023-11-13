import unittest

from cli_snake_game.food import Food


class TestFood(unittest.TestCase):
    def test_init(self):
        position = (50, 50)
        food = Food(position)
        self.assertEqual(food.position, position)

    def test_init_default(self):
        food = Food()
        self.assertEqual(food.position, (100, 100))

    def test_generate(self):
        food = Food()
        food.generate()
        self.assertIsInstance(food.position, tuple)
        self.assertEqual(len(food.position), 2)
        self.assertIsInstance(food.position[0], int)
        self.assertIsInstance(food.position[1], int)


if __name__ == "__main__":
    unittest.main()
