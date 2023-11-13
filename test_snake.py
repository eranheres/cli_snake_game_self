import unittest
from unittest.mock import patch
from cli_snake_game.snake import Snake

class TestSnake(unittest.TestCase):
    def test_init(self):
        snake = Snake([(50, 50), (40, 50), (30, 50)], "UP")
        self.assertEqual(snake.body, [(50, 50), (40, 50), (30, 50)])
        self.assertEqual(snake.direction, "UP")

        snake = Snake()
        self.assertEqual(snake.body, [(40, 40), (30, 40), (20, 40)])
        self.assertEqual(snake.direction, "RIGHT")

    def test_move(self):
        snake = Snake([(50, 50), (40, 50), (30, 50)], "UP")
        self.assertFalse(snake.move())
        self.assertEqual(snake.body, [(50, 40), (50, 50), (40, 50)])

        snake.direction = "DOWN"
        self.assertTrue(snake.move())

    def test_grow(self):
        snake = Snake([(50, 50), (40, 50), (30, 50)], "UP")
        snake.grow()
        self.assertEqual(snake.body, [(50, 50), (40, 50), (30, 50), (30, 50)])

    def test_check_collision(self):
        snake = Snake([(50, 50), (40, 50), (30, 50)], "UP")
        self.assertFalse(snake.check_collision())

        snake.body.append((50, 50))
        self.assertTrue(snake.check_collision())

if __name__ == '__main__':
    unittest.main()
