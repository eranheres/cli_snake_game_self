import unittest
from cli_snake_game.food import Food

class TestFood(unittest.TestCase):
    def test_init(self):
        food = Food()
        self.assertEqual(food.position, (100, 100))

        custom_position = (50, 50)
        food = Food(custom_position)
        self.assertEqual(food.position, custom_position)

    def test_generate(self):
        food = Food()
        for _ in range(100):
            old_position = food.position
            food.generate()
            self.assertNotEqual(food.position, old_position)
            self.assertTrue(0 <= food.position[0] <= 790)
            self.assertTrue(0 <= food.position[1] <= 590)

if __name__ == '__main__':
    unittest.main()
