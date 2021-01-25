from django.contrib import admin

# Register your models here.
from core.models import Event


class AdminEvent(admin.ModelAdmin):
    list_display = ('title', 'date', 'created_at')
    list_filter = ('title',)


admin.site.register(Event, AdminEvent)
