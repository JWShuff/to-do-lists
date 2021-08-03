from django import forms
from .models import Task, TodoList


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'due_date', 'list')


class TodoListForm(forms.ModelForm):
    class Meta:
        model = TodoList
        fields = ('list_name',)