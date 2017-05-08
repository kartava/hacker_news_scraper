# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scraper.utils import item_to_model, get_or_create


class ScraperPipeline(object):
    def process_item(self, item, spider):
        try:
            item_model = item_to_model(item)
        except TypeError:
            return item

        model, created = get_or_create(item_model)
        if created:
            return item.save()
