from django.db import models
from django.utils import timezone

# Create your models here.

## list
class TodoList(models.Model):
    list_name = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)
    #owner = models.ForeignKey(User) 

    def __str__(self):
        return f"""
        title: {self.list_name}
        """


##task
class Task(models.Model):
    title = models.CharField(max_length=255)
    due_date = models.DateTimeField(default=timezone.now)
    list = models.ForeignKey(
        TodoList,
        related_name='tasks',
        on_delete=models.CASCADE,
        null=True
        )
    ##owner = models.ForeignKey(User)

    def __str__(self):
        return f"""
        Task: {self.title}
        Due: {self.due_date}
        On List: {self.list} 
        """
    

