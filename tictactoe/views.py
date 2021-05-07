from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from tictactoe import enums
from tictactoe.models import TicTacToeGame
from tictactoe.serializers import GameGetSerializer, GameMoveSerializer
from tictactoe.services.game_service import reset_game, perform_game_move, start_game
from xo.permissions import IsAuthed


class GameGetView(APIView):
    permission_classes = (IsAuthed,)

    def get(self, request):
        game, _ = TicTacToeGame.objects.get_or_create(user=request.user_id)
        return Response(GameGetSerializer(instance=game).data)


class GameStartView(APIView):
    permission_classes = (IsAuthed,)

    def post(self, request):
        game, _ = TicTacToeGame.objects.get_or_create(user=request.user_id)
        start_game(game)
        return Response(GameGetSerializer(instance=game).data)


class GameResetView(APIView):
    permission_classes = (IsAuthed,)

    def post(self, request):
        game, _ = TicTacToeGame.objects.get_or_create(user=request.user_id)
        reset_game(game)
        return Response(GameGetSerializer(instance=game).data)


class GameMoveView(APIView):
    permission_classes = (IsAuthed,)

    def post(self, request):
        serializer = GameMoveSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        game, _ = TicTacToeGame.objects.get_or_create(user=request.user_id)
        move_valid, game = perform_game_move(game, serializer.validated_data['move_index'])
        if not move_valid:
            return Response('Cannot perform move', 400)

        return Response(GameGetSerializer(instance=game).data)


