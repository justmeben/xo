from django.db import models


class GameState(models.IntegerChoices):
    NOT_STARTED = 1
    ONGOING = 2
    FINISHED = 3


class WinnerState(models.IntegerChoices):
    NONE = 1
    PLAYER = 2
    COMPUTER = 3
    TIE = 4


class PlayerType(models.IntegerChoices):
    NONE = 0
    PLAYER = 1
    COMPUTER = 2
