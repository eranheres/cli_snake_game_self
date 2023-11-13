import unittest
from unittest.mock import patch
from cli_snake_game.main import main

class TestMain(unittest.TestCase):
    @patch('cli_snake_game.main.Game')
    def test_main(self, mock_game):
        main()
        mock_game.assert_called_once()
        mock_game.return_value.start_game.assert_called_once()
        mock_game.return_value.end_game.assert_called_once()

if __name__ == '__main__':
    unittest.main()
