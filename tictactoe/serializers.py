import json
from abc import ABC

from rest_framework import serializers

from tictactoe import enums
from tictactoe.models import TicTacToeGame


class GameGetSerializer(serializers.ModelSerializer):
    winner_state = serializers.SerializerMethodField()
    game_state = serializers.SerializerMethodField()
    board_state = serializers.SerializerMethodField()
    board_visual = serializers.SerializerMethodField()

    def get_winner_state(self, game):
        return enums.WinnerState(game.winner_state).name

    def get_game_state(self, game):
        return enums.GameState(game.game_state).name

    def get_board_state(self, game):
        return json.loads(game.board_state) if game.board_state else None

    def get_board_visual(self, game):
        state = json.loads(game.board_state) if game.board_state else None
        if state:
            return ("[%s] [%s] [%s]\n[%s] [%s] [%s]\n[%s] [%s] [%s]" % tuple(state)).replace('0', ' ').replace('1', 'X').replace('2', 'O')
        return ''

    class Meta:
        model = TicTacToeGame
        fields = ('winner_state', 'game_state', 'board_state', 'board_visual')


class GameMoveSerializer(serializers.Serializer):
    move_index = serializers.IntegerField(required=True, allow_null=False, min_value=0, max_value=8)
