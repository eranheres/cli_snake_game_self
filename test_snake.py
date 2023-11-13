import unittest
from unittest.mock import patch
from cli_snake_game.snake import Snake

class TestSnake(unittest.TestCase):
    def setUp(self):
        self.snake = Snake()

    def test_init(self):
        self.assertEqual(self.snake.body, [(40, 40), (30, 40), (20, 40)])
        self.assertEqual(self.snake.direction, "RIGHT")

    def test_move(self):
        initial_head = self.snake.body[0]
        self.snake.move()
        new_head = self.snake.body[0]
        self.assertNotEqual(initial_head, new_head)
        self.assertEqual(new_head, (50, 40))

    def test_grow(self):
        initial_length = len(self.snake.body)
        self.snake.grow()
        new_length = len(self.snake.body)
        self.assertEqual(new_length, initial_length + 1)

    def test_check_collision(self):
        self.snake.body = [(40, 40), (40, 40)]
        self.assertTrue(self.snake.check_collision())

if __name__ == '__main__':
    unittest.main()
