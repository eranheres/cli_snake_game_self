import unittest
from unittest.mock import Mock, patch
from cli_snake_game.game import Game

class TestGame(unittest.TestCase):
    @patch('pygame.init')
    @patch('pygame.display.set_mode')
    @patch('pygame.time.Clock')
    def test_init(self, mock_clock, mock_set_mode, mock_init):
        game = Game()
        mock_init.assert_called_once()
        mock_set_mode.assert_called_once_with((800, 600))
        mock_clock.assert_called_once()
        self.assertEqual(game.score, 0)
        self.assertFalse(game.game_over)
        self.assertIsInstance(game.snake, Snake)
        self.assertIsInstance(game.food, Food)

    @patch('pygame.font.Font')
    def test_render_score(self, mock_font):
        game = Game()
        game.score = 5
        game.render_score()
        mock_font.assert_called_once_with(None, 36)
        self.assertTrue(mock_font.return_value.render.called)

    @patch('pygame.event.get')
    def test_start_game(self, mock_get):
        game = Game()
        mock_get.return_value = [Mock(type=pygame.QUIT)]
        game.start_game()
        self.assertTrue(game.game_over)

    @patch('pygame.quit')
    def test_end_game(self, mock_quit):
        game = Game()
        game.end_game()
        mock_quit.assert_called_once()

    @patch('pygame.display.flip')
    def test_update_display(self, mock_flip):
        game = Game()
        game.update_display()
        mock_flip.assert_called_once()

if __name__ == '__main__':
    unittest.main()
