import pytest

from src.game import Game, Turn


@pytest.fixture
def game():
    return Game(
        "Game 1: 4 red, 3 blue; 6 blue, 16 green; 9 blue, 13 green, 1 red; 10 green, 4 red, 6 blue"
    )


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

    def test_game_id(self):
        game = Game("Game 1:")
        assert game.identification == 1

        game = Game("Game 77:")
        assert game.identification == 77

    def test_parsing(self, game):
        assert len(game.turns) == 4
        assert game.turns[0] == Turn(4, 0, 3)
        assert game.turns[1] == Turn(0, 16, 6)
        assert game.turns[2] == Turn(1, 13, 9)
        assert game.turns[3] == Turn(4, 10, 6)

    def test_possibility(self, game):
        assert game.is_possible(20, 20, 20)
        assert not game.is_possible(1, 1, 1)

        assert not game.is_possible(3, 20, 20)
        assert not game.is_possible(20, 15, 20)
        assert not game.is_possible(20, 20, 8)
        assert game.is_possible(4, 16, 9)

    def test_min_allowed(self, game):
        assert game.min_allowed() == (4, 16, 9)
