from rest_framework import viewsets
from rest_framework.parsers import JSONParser, FormParser, MultiPartParser
from rest_framework.permissions import IsAuthenticated
from DRF.apipoint.models import CustomUser
from DRF.apipoint.serialiazers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    parser_classes = [JSONParser, FormParser, MultiPartParser]
    permission_classes = [IsAuthenticated]