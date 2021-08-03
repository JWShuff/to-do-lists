from django.urls import path, include
from .views import TaskViewSet, TodoListViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')
router.register(r'todolist', TodoListViewSet, basename='todolist')

urlpatterns = router.urls
