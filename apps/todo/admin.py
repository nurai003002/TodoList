from django.contrib import admin

from apps.todo.models import Task
# Register your models here.

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title','description', 'completed', 'created')
    list_filter = ('title','description', 'completed', 'created')