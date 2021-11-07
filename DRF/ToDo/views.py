from django.http import Http404
from rest_framework import viewsets, mixins, status
from rest_framework.parsers import JSONParser, FormParser, MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .filters import ProjectFilter, PresentToDoFilter, CRUDToDoFilter
from .models import Project, ToDo
from .paginator import ProjectLimitOffsetPagination, ToDoLimitOffsetPagination
from .serialiazers import PresentProjectSerializer, CRUDProjectSerializer, CRUDToDoSerializer, PresentToDoSerializer

class PresentProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = PresentProjectSerializer
    parser_classes = [JSONParser, FormParser, MultiPartParser]
    pagination_class = ProjectLimitOffsetPagination
    filterset_class = ProjectFilter
    # permission_classes = [IsAuthenticated]

class CRUDProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = CRUDProjectSerializer
    parser_classes = [JSONParser, FormParser, MultiPartParser]
    pagination_class = ProjectLimitOffsetPagination
    filterset_class = ProjectFilter
    # permission_classes = [IsAuthenticated]

class PresentToDoViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = ToDo.objects.all()
    serializer_class = PresentToDoSerializer
    parser_classes = [JSONParser, FormParser, MultiPartParser]
    pagination_class = ToDoLimitOffsetPagination
    filterset_class = PresentToDoFilter
    # permission_classes = [IsAuthenticated]

class CRUDToDoViewSet(mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = ToDo.objects.all()
    serializer_class = CRUDToDoSerializer
    parser_classes = [JSONParser, FormParser, MultiPartParser]
    pagination_class = ToDoLimitOffsetPagination
    filterset_class = CRUDToDoFilter
    # permission_classes = [IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        id = self.kwargs['pk']
        try:
            ToDo.objects.filter(id=int(id)).update(status=False)
        except Http404:
            pass
        return Response(status=status.HTTP_204_NO_CONTENT)


