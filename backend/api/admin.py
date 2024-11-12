from django.contrib import admin
from .models import University, Program, FAQ


@admin.register(University)
class UniversityAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'website')
    search_fields = ('name', 'location')
    list_filter = ('location',)  
    ordering = ('name',)  


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('name', 'university', 'tuition_fee', 'duration', 'language_of_instruction')
    list_filter = ('university', 'language_of_instruction', 'duration')
    search_fields = ('name', 'university__name')
    ordering = ('name', 'university')


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'program')
    search_fields = ('question', 'answer', 'program__name')
    list_filter = ('program',)
    ordering = ('program', 'question')
