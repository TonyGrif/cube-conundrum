import pytest
from src.game import Turn, Game

class TestGameClass:
    def test_turn(self):
        turn = Turn(3, 3, 3)
        assert turn.red == 3
        assert turn.green == 3
        assert turn.blue == 3

        turn = Turn(12, 13, 14)
        assert turn.red == 12
        assert turn.green == 13
        assert turn.blue == 14

    def test_game(self):
        pass
