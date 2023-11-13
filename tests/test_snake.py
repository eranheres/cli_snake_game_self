import unittest
from cli_snake_game import snake

class TestSnake(unittest.TestCase):
    def setUp(self):
        self.snake = snake.Snake()

    def test_init(self):
        self.assertEqual(self.snake.body, [(40, 40), (30, 40), (20, 40)])
        self.assertEqual(self.snake.direction, "RIGHT")
        self.assertEqual(len(self.snake.body), 3)

    def test_move(self):
        self.snake.move()
        self.assertEqual(self.snake.body[0], (50, 40))
        self.snake.direction = "UP"
        self.snake.move()
        self.assertEqual(self.snake.body[0], (50, 30))

    def test_grow(self):
        self.snake.grow()
        self.assertEqual(len(self.snake.body), 4)

    def test_check_collision(self):
        self.snake.body = [(40, 40), (40, 40)]
        self.assertTrue(self.snake.check_collision())

class TestFood(unittest.TestCase):
    def setUp(self):
        self.food = snake.Food()

    def test_init(self):
        self.assertEqual(self.food.position, (100, 100))

    def test_generate(self):
        self.food.generate()
        self.assertTrue(0 <= self.food.position[0] <= 790)
        self.assertTrue(0 <= self.food.position[1] <= 590)

if __name__ == "__main__":
    unittest.main()
