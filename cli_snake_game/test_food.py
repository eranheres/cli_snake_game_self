import unittest
from food import Food

class TestFood(unittest.TestCase):
    def test_init(self):
        food = Food((100, 100))
        self.assertEqual(food.position, (100, 100))

    def test_generate(self):
        food = Food()
        food.generate()
        x, y = food.position
        self.assertTrue(0 <= x <= 790 and x % 10 == 0)
        self.assertTrue(0 <= y <= 590 and y % 10 == 0)

if __name__ == '__main__':
    unittest.main()
