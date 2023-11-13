import unittest

from snake import Snake


class TestSnake(unittest.TestCase):
    def setUp(self):
        self.snake = Snake([(40, 40), (30, 40), (20, 40)], "RIGHT")

    def test_move(self):
        self.snake.move()
        self.assertEqual(self.snake.body[0], (50, 40))
        self.snake.direction = "UP"
        self.snake.move()
        self.assertEqual(self.snake.body[0], (50, 30))

    def test_grow(self):
        old_length = len(self.snake.body)
        self.snake.grow()
        self.assertEqual(len(self.snake.body), old_length + 1)

    def test_check_collision(self):
        self.snake.body[0] = (30, 40)
        self.assertTrue(self.snake.check_collision())
        self.snake.body[0] = (50, 40)
        self.assertFalse(self.snake.check_collision())


if __name__ == "__main__":
    unittest.main()
