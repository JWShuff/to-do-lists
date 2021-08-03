from rest_framework import viewsets
from .models import Task, TodoList
from .forms import TaskForm, TodoListForm
from .serializers import TaskSerializer, TodoListSerializer
from rest_framework.response import Response

class TodoListViewSet(viewsets.ModelViewSet):
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset=Task.objects.all()
    serializer_class=TaskSerializer
