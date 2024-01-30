from rest_framework.routers import DefaultRouter

from apps.todo.views import TaskAPI

router = DefaultRouter()

router.register('task', TaskAPI, basename='api_task')

urlpatterns = router.urls
