import graphene
from graphene_django import DjangoObjectType
from .models import ToDo, Project
from apipoint.models import CustomUser

class ToDoType(DjangoObjectType):
    class Meta:
        model = ToDo
        fields = '__all__'

class ProjectType(DjangoObjectType):
    class Meta:
        model = Project
        fields = '__all__'

class CreatorType(DjangoObjectType):
    class Meta:
        model = CustomUser
        fields = '__all__'


class Query(graphene.ObjectType):
    projects = graphene.List(ProjectType)
    creators = graphene.List(CreatorType)
    todos = graphene.List(ToDoType)
    todo_project = graphene.Field(ToDoType, id=graphene.Int(required=True))
    todo_creator = graphene.Field(ToDoType, id=graphene.Int(required=True))

    def resolve_todos(self, info, **kwargs):
        return ToDo.objects.all()

    def resolve_projects(self, info, **kwargs):
        return Project.objects.all()

    def resolve_creators(self, info, **kwargs):
        return CustomUser.objects.all()

    def resolve_todo_project_by_id(self, info, id):
        try:
            return ToDo.objects.get(id=id).project
        except ToDo.DoesNotExist:
            return None

    def resolve_todo_creator_by_id(self, info, id):
        try:
            return ToDo.objects.get(id=id).creator
        except ToDo.DoesNotExist:
            return None

