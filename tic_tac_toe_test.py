import pytest
from tic_tac_toe import TicTacToe, HumanPlayer


def test_tic_tac_toe_winner_horizontal():
    game = TicTacToe()
    game.make_move(0, 'X')
    game.make_move(1, 'X')
    game.make_move(2, 'X')
    assert game.current_winner == 'X'


def test_tic_tac_toe_winner_vertical():
    game = TicTacToe()
    game.make_move(0, 'O')
    game.make_move(3, 'O')
    game.make_move(6, 'O')
    assert game.current_winner == 'O'


def test_tic_tac_toe_winner_diagonal():
    game = TicTacToe()
    game.make_move(0, 'X')
    game.make_move(4, 'X')
    game.make_move(8, 'X')
    assert game.current_winner == 'X'


def test_tic_tac_toe_draw():
    game = TicTacToe()
    game.make_move(0, 'X')
    game.make_move(1, 'O')
    game.make_move(2, 'X')
    game.make_move(3, 'O')
    game.make_move(4, 'X')
    game.make_move(5, 'O')
    game.make_move(6, 'O')
    game.make_move(7, 'X')
    game.make_move(8, 'O')
    assert game.current_winner is None


def test_human_player_get_move():
    player = HumanPlayer('X')
    with pytest.raises(ValueError):
        player.get_move(TicTacToe())  # Input outside of range
    with pytest.raises(ValueError):
        player.get_move(TicTacToe())  # Invalid input type
