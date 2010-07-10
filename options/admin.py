# -*- coding: utf-8 -*-
__author__="PyKaB"
__date__ ="$28.05.2009 20:11:03$"
from django.contrib import admin
from options.models import Option

class OptionAdmin(admin.ModelAdmin):
    list_display = ('okey', 'ovalue', 'help', 'proccessed')
    list_editable = ('ovalue', 'proccessed')
    ordering = ('okey',)

admin.site.register(Option, OptionAdmin)