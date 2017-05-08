# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from hacker_news_scraper.posts.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'author',
        'url',
        'site'
    )
    search_fields = (
        'title',
    )
