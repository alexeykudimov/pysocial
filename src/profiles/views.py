from rest_framework.generics import RetrieveAPIView, UpdateAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from .models import SocUser
from .serializers import GetSocUserSerializer, GetSocUserPublicSerializer

class SocUserPublicView(ModelViewSet):
    # Вывод публичного профиля пользователя
    queryset = SocUser.objects.all()
    serializer_class = GetSocUserPublicSerializer
    permissions_classes = [permissions.AllowAny]


class SocUserView(ModelViewSet):
    # Вывод профиля пользователя
    serializer_class = GetSocUserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return SocUser.objects.filter(id=self.request.user.id)