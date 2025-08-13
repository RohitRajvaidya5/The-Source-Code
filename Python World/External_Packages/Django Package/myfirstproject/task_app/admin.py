from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "short_description", "completed")
    list_filter = ("completed",)
    search_fields = ("title",)
    ordering = ("-completed", "title")
    list_display_links = ("title",)

    def short_description(self, obj):
        return (obj.description[:50] + "...") if len(obj.description) > 50 else obj.description
    short_description.short_description = "Description"
