from rest_framework import serializers
from .models import TodoList, Task


class TodoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoList
        fields = ['list_name', 'created_date', 'tasks']
        depth = 1


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['title', 'due_date', 'list']
        depth = 1


