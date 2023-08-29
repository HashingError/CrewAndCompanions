from django.contrib import admin
from .models import Letter
# Register your models here.


class LetterAdmin(admin.ModelAdmin):
    list_filter = ['publish', 'reviewed']
    list_display = ['preview', 'publish', 'reviewed']
    date_hierarchy = 'submitted'
    ordering = ('submitted',)

    def preview(self, obj):
        return f'{obj.displayed_name} | {obj.message[:50]}'


admin.site.register(Letter, LetterAdmin)
