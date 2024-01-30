from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

from apps.todo.models import Task
from apps.todo.serializers import TaskSerializer

class TaskAPI(GenericViewSet,
              mixins.ListModelMixin,
              mixins.CreateModelMixin,
              mixins.UpdateModelMixin,
              mixins.RetrieveModelMixin,
              mixins.DestroyModelMixin,
              ):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    
