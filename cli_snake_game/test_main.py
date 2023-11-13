import unittest
from unittest.mock import patch, MagicMock
from cli_snake_game.main import main
from cli_snake_game.game import Game

class TestMain(unittest.TestCase):
    @patch.object(Game, 'start_game')
    @patch.object(Game, 'end_game')
    @patch('cli_snake_game.main.Game', autospec=True)
    def test_main(self, mock_game, mock_end_game, mock_start_game):
        mock_game_instance = mock_game.return_value
        mock_game_instance.start_game = MagicMock()
        mock_game_instance.end_game = MagicMock()
        
        main()
        
        mock_start_game.assert_called_once()
        mock_end_game.assert_called_once()

if __name__ == '__main__':
    unittest.main()
