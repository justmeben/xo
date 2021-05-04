import json
import random

from tictactoe import enums
from tictactoe.models import TicTacToeGame


def start_game(game: TicTacToeGame):
    """
    Starts game object and saves to db
    :param game: TicTacToeGame
    :return:
    """
    game.winner_state = enums.WinnerState.NONE.value
    game.game_state = enums.GameState.ONGOING.value
    game.board_state = json.dumps([enums.PlayerType.NONE.value for _ in range(9)])
    game.save()


def reset_game(game: TicTacToeGame):
    """
    Resets game object and saves to db
    :param game: TicTacToeGame
    :return:
    """
    game.winner_state = enums.WinnerState.NONE.value
    game.game_state = enums.GameState.NOT_STARTED.value
    game.board_state = None
    game.save()


def perform_game_move(game: TicTacToeGame, move_index: int) -> tuple:
    """
    Performs a player input move into game, validates, checks for win, etc...
    :param game: TicTacToeGame
    :param move_index: index representing where the place placed their move, 0-8
    :return: tuple: (is_valid, updated TicTacToeGame instance)
    """

    def get_super_computer_move(state: list):
        available_indexes = [x[0] for x in enumerate(state) if x[1] == enums.PlayerType.NONE.value]
        return random.choice(available_indexes)

    def check_win(state: list):
        """
        Easier to visualize:
        [[0, 1, 2],
         [3, 4, 5],
         [6, 7, 8]]
        """
        is_row_0 = state[0] == state[1] and state[1] == state[2]
        is_row_1 = state[3] == state[4] and state[4] == state[5]
        is_row_2 = state[6] == state[7] and state[7] == state[8]
        is_col_0 = state[0] == state[3] and state[3] == state[6]
        is_col_1 = state[1] == state[4] and state[4] == state[7]
        is_col_2 = state[2] == state[5] and state[5] == state[8]
        is_diag_0 = state[0] == state[4] and state[4] == state[8]
        is_diag_1 = state[2] == state[4] and state[4] == state[6]

        for player_type, winner_state in [(enums.PlayerType.PLAYER.value, enums.WinnerState.PLAYER.value),
                                          (enums.PlayerType.COMPUTER.value, enums.WinnerState.COMPUTER.value)]:
            if (state[0] == player_type and (is_row_0 or is_col_0 or is_diag_0)) or \
                    (state[5] == player_type and (is_row_1 or is_col_2)) or \
                    (state[7] == player_type and (is_row_2 or is_col_1)) or \
                    (state[2] == player_type and is_diag_1):
                return winner_state

        if not [x for x in state if x == enums.PlayerType.NONE.value]:
            return enums.WinnerState.TIE

        return enums.WinnerState.NONE

    # Validate game is ongoing
    if game.game_state != enums.GameState.ONGOING.value:
        return False, game

    # json.loads because of TextField
    board_state = json.loads(game.board_state)

    # Check if move is valid
    if board_state[move_index] != enums.PlayerType.NONE.value:
        return False, game

    # Perform Player move & Check win
    board_state[move_index] = enums.PlayerType.PLAYER.value
    winner_state = check_win(board_state)

    # Perform Computer move (if winner is not decided) & Check win
    if winner_state == enums.WinnerState.NONE.value:
        super_computer_move = get_super_computer_move(board_state)
        board_state[super_computer_move] = enums.PlayerType.COMPUTER.value
        winner_state = check_win(board_state)

    # Updating game instance
    game.winner_state = winner_state
    game.game_state = enums.GameState.ONGOING.value if winner_state == enums.WinnerState.NONE.value else enums.GameState.FINISHED.value
    game.board_state = json.dumps(board_state)
    game.save()

    return True, game
