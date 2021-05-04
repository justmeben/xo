from django.contrib.auth.models import User
from django.db import models
from tictactoe import enums


class TicTacToeGame(models.Model):
    user = models.ForeignKey(User, null=False, blank=False, on_delete=models.DO_NOTHING)
    winner_state = models.IntegerField(choices=enums.WinnerState.choices, null=False, blank=False,
                                       default=enums.WinnerState.NONE.value)
    game_state = models.IntegerField(choices=enums.GameState.choices, null=False, blank=False,
                                     default=enums.GameState.NOT_STARTED.value)

    # Ideally a json field, there isn't a difference in this use case since we are not querying inside this field
    # this is a TextField because of sqlite db limitations
    # Example field content: [0, 0, 1, 2, 0, 2, 2, 1, 0]
    board_state = models.TextField(null=True, blank=True)
