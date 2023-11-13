import unittest

from cli_snake_game import snake


class TestSnake(unittest.TestCase):
    def test_init(self):
        s = snake.Snake()
        self.assertEqual(s.body, [(40, 40), (30, 40), (20, 40)])
        self.assertEqual(s.direction, "RIGHT")

    def test_move(self):
        s = snake.Snake()
        s.move()
        self.assertEqual(s.body[0], (50, 40))
        s.direction = "UP"
        s.move()
        self.assertEqual(s.body[0], (50, 30))

    def test_grow(self):
        s = snake.Snake()
        s.grow()
        self.assertEqual(len(s.body), 4)

    def test_check_collision(self):
        s = snake.Snake([(40, 40), (30, 40), (40, 40)])
        self.assertTrue(s.check_collision())


class TestFood(unittest.TestCase):
    def test_init(self):
        f = snake.Food()
        self.assertEqual(f.position, (100, 100))

    def test_generate(self):
        f = snake.Food()
        f.generate()
        self.assertTrue(0 <= f.position[0] <= 790)
        self.assertTrue(0 <= f.position[1] <= 590)


if __name__ == "__main__":
    unittest.main()
