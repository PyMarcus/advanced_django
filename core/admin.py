from django.contrib import admin
from .models import Services, Profission, Team


@admin.register(Profission)
class ProfissionAdmin(admin.ModelAdmin):
    list_display = ('profission', 'active', 'modified', 'create')


@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('service', 'description', 'icon', 'active', 'modified', 'create')


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'description','profission','facebook', 'twitter','instagram',
                    'image','active', 'modified', 'create')
