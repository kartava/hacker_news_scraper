# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy_djangoitem import DjangoItem

from hacker_news_scraper.posts.models import Post


class SpiderItem(DjangoItem):
    django_model = Post
