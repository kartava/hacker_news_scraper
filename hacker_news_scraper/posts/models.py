# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255, null=True)
    url = models.URLField(max_length=500)
    site = models.URLField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return ('%s' % self.title).encode('ascii', errors='replace')
