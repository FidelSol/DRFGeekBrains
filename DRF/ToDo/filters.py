from django_filters import rest_framework as filters
from .models import Project, ToDo

class ProjectFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='contains')

    class Meta:
       model = Project
       fields = ['name']

class PresentToDoFilter(filters.FilterSet):
    add_time_gte = filters.DateTimeFilter(field_name="add_time", lookup_expr='gte')
    add_time_lte = filters.DateTimeFilter(field_name="add_time", lookup_expr='lte')

    class Meta:
       model = ToDo
       fields = ['project__name', 'add_time_gte', 'add_time_lte']

class CRUDToDoFilter(filters.FilterSet):

    class Meta:
       model = ToDo
       fields = ['project']