import unittest

from cli_snake_game.snake import Food, Snake


class SnakeTest(unittest.TestCase):
    def test_init(self):
        snake = Snake()
        self.assertEqual(len(snake.body), 3)
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
        snake = Snake([(40, 40), (30, 40), (40, 40)])
        self.assertTrue(snake.check_collision())


class FoodTest(unittest.TestCase):
    def test_init(self):
        food = Food()
        self.assertEqual(food.position, (100, 100))

    def test_generate(self):
        food = Food()
        food.generate()
        self.assertTrue(0 <= food.position[0] <= 790)
        self.assertTrue(0 <= food.position[1] <= 590)


if __name__ == "__main__":
    unittest.main()
    def test_grow_beyond_boundaries(self):
        snake = Snake([(790, 590)], "RIGHT")
        snake.grow()
        self.assertEqual(snake.body[-1], (790, 590))
        self.assertTrue(snake.move())

    def test_generate_on_snake(self):
        snake = Snake([(i * 10, 0) for i in range(80)])  # Snake occupies the entire top row
        food = Food((0, 0))
        for _ in range(1000):  # Test multiple times to reduce chance of false positives
            food.generate()
            self.assertNotIn(food.position, snake.body)
        food = Food()
        self.assertEqual(food.position, (100, 100))

    def test_generate_within_boundaries(self):
        food = Food()
        for _ in range(1000):  # Test multiple times to reduce chance of false positives
            food.generate()
            self.assertTrue(0 <= food.position[0] <= 790)
            self.assertTrue(0 <= food.position[1] <= 590)
    
    def test_generate_not_on_snake(self):
        snake = Snake([(i * 10, 0) for i in range(80)])  # Snake occupies the entire top row
        food = Food()
        for _ in range(1000):  # Test multiple times to reduce chance of false positives
            food.generate()
            self.assertNotIn(food.position, snake.body)


if __name__ == "__main__":
    unittest.main()
        self.assertEqual(len(snake.body), 4)

    def test_check_collision(self):
        snake = Snake([(40, 40), (30, 40), (40, 40)])
        self.assertTrue(snake.check_collision())


class FoodTest(unittest.TestCase):
    def test_init_default(self):
        food = Food()
        self.assertEqual(food.position, (100, 100))
    
    def test_init_custom(self):
        food = Food((200, 200))
        self.assertEqual(food.position, (200, 200))

    def test_generate(self):
        food = Food()
        food.generate()
        self.assertTrue(0 <= food.position[0] <= 790)
        self.assertTrue(0 <= food.position[1] <= 590)


if __name__ == "__main__":
    unittest.main()
        self.assertEqual(len(snake.body), 4)

    def test_check_collision(self):
        snake = Snake([(40, 40), (30, 40), (40, 40), (30, 40)])
        self.assertTrue(snake.check_collision())


class FoodTest(unittest.TestCase):
    def test_init(self):
        food = Food()
        self.assertEqual(food.position, (100, 100))

    def test_generate(self):
        food = Food()
        food.generate()
        self.assertTrue(0 <= food.position[0] <= 790)
        self.assertTrue(0 <= food.position[1] <= 590)


if __name__ == "__main__":
    unittest.main()
        snake = Snake([(50, 50)])
        snake.grow()
        self.assertEqual(len(snake.body), 2)
        self.assertEqual(snake.body[-1], (50, 50))

    def test_check_collision(self):
        snake = Snake([(40, 40), (30, 40), (40, 40)])
        self.assertTrue(snake.check_collision())


class FoodTest(unittest.TestCase):
    def test_init(self):
        food = Food()
        self.assertEqual(food.position, (100, 100))

    def test_generate(self):
        food = Food()
        food.generate()
        self.assertTrue(0 <= food.position[0] <= 790)
        self.assertTrue(0 <= food.position[1] <= 590)


if __name__ == "__main__":
    unittest.main()
        snake = Snake([(50, 50)])
        snake.direction = "UP"
        snake.move()
        self.assertEqual(snake.body[0], (50, 40))
        snake.direction = "DOWN"
        snake.move()
        self.assertEqual(snake.body[0], (50, 50))
        snake.direction = "LEFT"
        snake.move()
        self.assertEqual(snake.body[0], (40, 50))
        snake.direction = "RIGHT"
        snake.move()
        self.assertEqual(snake.body[0], (50, 50))
    
    def test_move_border_collision(self):
        snake = Snake([(0, 0)], "LEFT")
        self.assertTrue(snake.move())
        snake = Snake([(0, 0)], "UP")
        self.assertTrue(snake.move())
        snake = Snake([(790, 590)], "RIGHT")
        self.assertTrue(snake.move())
        snake = Snake([(790, 590)], "DOWN")
        self.assertTrue(snake.move())

    def test_grow(self):
        snake = Snake()
        snake.grow()
        self.assertEqual(len(snake.body), 4)

    def test_check_collision(self):
        snake = Snake([(40, 40), (30, 40), (40, 40)])
        self.assertTrue(snake.check_collision())


class FoodTest(unittest.TestCase):
    def test_init(self):
        food = Food()
        self.assertEqual(food.position, (100, 100))

    def test_generate(self):
        food = Food()
        food.generate()
        self.assertTrue(0 <= food.position[0] <= 790)
        self.assertTrue(0 <= food.position[1] <= 590)


if __name__ == "__main__":
    unittest.main()
        snake = Snake()
        self.assertEqual(len(snake.body), 3)
        self.assertEqual(snake.body, [(40, 40), (30, 40), (20, 40)])
        self.assertEqual(snake.direction, "RIGHT")
    
    def test_init_custom(self):
        snake = Snake([(10, 10), (20, 20), (30, 30)], "LEFT")
        self.assertEqual(len(snake.body), 3)
        self.assertEqual(snake.body, [(10, 10), (20, 20), (30, 30)])
        self.assertEqual(snake.direction, "LEFT")

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
        snake = Snake([(40, 40), (30, 40), (40, 40)])
        self.assertTrue(snake.check_collision())


class FoodTest(unittest.TestCase):
    def test_init(self):
        food = Food()
        self.assertEqual(food.position, (100, 100))

    def test_generate(self):
        food = Food()
        food.generate()
        self.assertTrue(0 <= food.position[0] <= 790)
        self.assertTrue(0 <= food.position[1] <= 590)


if __name__ == "__main__":
    unittest.main()
