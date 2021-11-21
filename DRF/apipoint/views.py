from rest_framework import viewsets, mixins
from rest_framework.parsers import JSONParser, FormParser, MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer

from .models import CustomUser
from .serialiazers import UserSerializer

class UserViewSet(mixins.UpdateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    parser_classes = [JSONParser, FormParser, MultiPartParser]
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    permission_classes = [IsAuthenticated]
