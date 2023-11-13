import unittest
from unittest.mock import patch, MagicMock
from cli_snake_game.main import main

class TestMain(unittest.TestCase):
    @patch('cli_snake_game.main.Game')
    def test_main(self, mock_game):
        mock_game_instance = mock_game.return_value
        main()
        mock_game.assert_called_once_with()
        mock_game_instance.start_game.assert_called_once_with()
        mock_game_instance.end_game.assert_called_once_with()

if __name__ == '__main__':
    unittest.main()
