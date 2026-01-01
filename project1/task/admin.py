from django.contrib import admin
from .models import Task
# Register your models here.


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'realized', 'due_date', 'created_at', 'updated_at')
    list_filter = ('realized', 'due_date', 'created_at')
    search_fields = ('title', 'description')
    ordering = ('-created_at',)