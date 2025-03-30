from django.contrib import admin
from .models import PartOfText


@admin.register(PartOfText)
class PartOfTextAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'created', 'updated']

