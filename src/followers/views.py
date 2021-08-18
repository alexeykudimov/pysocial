from rest_framework import generics, permissions, views
from rest_framework.response import Response
from src.profiles.models import SocUser
from .models import Follower
from .serializers import ListFollowerSerializer


class ListFollowerView(generics.ListAPIView):
    # вывод списка подписчиков пользователя

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ListFollowerSerializer

    def get_queryset(self):
        return Follower.objects.filter(user=self.request.user)

class FollowerView(views.APIView):
    # Добавление/удаление подписчиков

    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        try:
            user = SocUser.objects.filter(id=pk)
        except Follower.DoesNotExist:
            return Response(status=404)

        Follower.objects.create(subscriber=request.user, user=user)
        return Response(status=201)

    def delete(self, request, pk):
        try:
            sub = Follower.objects.get(subscriber=request.user, user_id=pk)
        except Follower.DoesNotExist:
            return Response(status=404)

        sub.delete()
        return Response(status=204)

