import unittest
from unittest.mock import patch

import pygame
from game import Game


class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    @patch("pygame.display.set_mode")
    @patch("pygame.event.get")
    def test_start_game(self, mock_get, mock_set_mode):
        mock_get.return_value = [pygame.event.Event(pygame.QUIT)]
        self.game.start_game()
        self.assertTrue(self.game.game_over)

    @patch("pygame.quit")
    def test_end_game(self, mock_quit):
        self.game.end_game()
        self.assertTrue(self.game.game_over)
        mock_quit.assert_called_once()

    @patch("pygame.display.flip")
    @patch("pygame.Surface.blit")
    def test_update_display(self, mock_blit, mock_flip):
        self.game.update_display()
        self.assertEqual(mock_blit.call_count, 7)
        mock_flip.assert_called_once()


if __name__ == "__main__":
    unittest.main()
