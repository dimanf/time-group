# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.flatpages.models import FlatPage
from django.contrib.flatpages.admin import FlatPageAdmin

class FlatPageAdmin(FlatPageAdmin):
    list_display = ('title', 'url',)
    fields = ('url', 'title', 'content', 'sites', 'template_name',)
    fieldsets = ()
    
    class Media:
        js = [
            '/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
            '/static/grappelli/tinymce_setup/tinymce_setup.js',
        ]