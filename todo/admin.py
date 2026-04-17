from django.contrib import admin
from .models import Task


# cereating task list
class TaskAdmin (admin.ModelAdmin):
    list_display = ('task', 'is_completed', 'updated_at')
    search_fields = ('task',)   #creating search field
    
# Registed my models from models.py here.
admin.site.register(Task, TaskAdmin)