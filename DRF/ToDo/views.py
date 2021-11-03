from rest_framework import viewsets
from rest_framework.parsers import JSONParser, FormParser, MultiPartParser
from rest_framework.permissions import IsAuthenticated
from .models import Project, ToDo
from .serialiazers import PresentProjectSerializer, CRUDProjectSerializer, CRUDToDoSerializer, PresentToDoSerializer


class PresentProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = PresentProjectSerializer
    parser_classes = [JSONParser, FormParser, MultiPartParser]
    # permission_classes = [IsAuthenticated]

class CRUDProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = CRUDProjectSerializer
    parser_classes = [JSONParser, FormParser, MultiPartParser]
    # permission_classes = [IsAuthenticated]

class PresentToDoViewSet(viewsets.ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = PresentToDoSerializer
    parser_classes = [JSONParser, FormParser, MultiPartParser]
    # permission_classes = [IsAuthenticated]

class CRUDToDoViewSet(viewsets.ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = CRUDToDoSerializer
    parser_classes = [JSONParser, FormParser, MultiPartParser]
    # permission_classes = [IsAuthenticated]