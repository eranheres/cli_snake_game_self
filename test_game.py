import unittest
from unittest.mock import Mock, patch
from cli_snake_game.game import Game

class TestGame(unittest.TestCase):
    @patch('cli_snake_game.game.pygame')
    @patch('cli_snake_game.game.Snake')
    @patch('cli_snake_game.game.Food')
    def setUp(self, mock_pygame, mock_snake, mock_food):
        self.game = Game()
        self.mock_pygame = mock_pygame
        self.mock_snake = mock_snake
        self.mock_food = mock_food

    def test_init(self):
        self.assertEqual(self.game.score, 0)
        self.assertEqual(self.game.game_over, False)
        self.mock_snake.assert_called_once()
        self.mock_food.assert_called_once()

    def test_render_score(self):
        self.game.render_score()
        self.mock_pygame.font.Font().render.assert_called_once_with('Score: 0', True, (255, 255, 255))

    def test_start_game(self):
        self.mock_pygame.event.get.return_value = [self.mock_pygame.QUIT]
        self.game.start_game()
        self.assertEqual(self.game.game_over, True)

    def test_end_game(self):
        self.game.end_game()
        self.mock_pygame.quit.assert_called_once()

    def test_update_display(self):
        self.game.update_display()
        self.assertEqual(self.mock_pygame.draw.rect.call_count, 6)
        self.mock_pygame.display.flip.assert_called_once()

if __name__ == '__main__':
    unittest.main()
