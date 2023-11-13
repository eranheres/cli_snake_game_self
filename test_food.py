import unittest
from unittest.mock import patch
from cli_snake_game.food import Food

class TestFood(unittest.TestCase):
    def test_init(self):
        food = Food((50, 50))
        self.assertEqual(food.position, (50, 50))

        food = Food()
        self.assertEqual(food.position, (100, 100))

    @patch('random.randint')
    def test_generate(self, mock_randint):
        mock_randint.side_effect = [5, 3]
        food = Food()
        food.generate()
        self.assertEqual(food.position, (50, 30))
