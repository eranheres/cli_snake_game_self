import unittest

from cli_snake_game.snake import Food, Snake


class TestSnake(unittest.TestCase):
    def test_init(self):
        snake = Snake([(40, 40), (30, 40), (20, 40)])
        self.assertEqual(snake.body, [(40, 40), (30, 40), (20, 40)])
        self.assertEqual(snake.direction, "RIGHT")

    def test_move(self):
        snake = Snake()
        snake.move()
        self.assertEqual(snake.body[0], (50, 40))
        snake.direction = "UP"
        snake.move()
        self.assertEqual(snake.body[0], (50, 30))

    def test_grow(self):
        snake = Snake()
        snake.grow()
        self.assertEqual(len(snake.body), 4)

    def test_check_collision(self):
        snake = Snake([(40, 40), (30, 40), (20, 40), (40, 40)])
        self.assertTrue(snake.check_collision())


class TestFood(unittest.TestCase):
    def test_init(self):
        food = Food()
        self.assertEqual(food.position, (100, 100))

    def test_generate(self):
        food = Food()
        food.generate()
        x, y = food.position
        self.assertTrue(0 <= x <= 790)
        self.assertTrue(0 <= y <= 590)


if __name__ == "__main__":
    unittest.main()
