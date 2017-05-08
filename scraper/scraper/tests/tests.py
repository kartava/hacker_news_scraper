import unittest
from itertools import islice

from scraper.spiders.hacker_news_spider import HackerNewsSpider

from scraper.tests import fake_response_from_file

from scraper.items import SpiderItem


class HackerNewsSpiderTest(unittest.TestCase):
    kwargs = {'author': None,
              'site': 'https://news.ycombinator.com/from?site=arxiv.org',
              'title': u'Structure of the Milky Way',
              'url': u'https://arxiv.org/abs/1309.4838'}

    def setUp(self):
        self.spider = HackerNewsSpider()
        self.fake_response = fake_response_from_file('_test_page.html')
        self.spider_item = SpiderItem(**self.kwargs)

    @staticmethod
    def _nth(iterable, n, default=None):
        # Returns the nth item or a default value
        return next(islice(iterable, n, None), default)

    def _test_item_results(self, results, expected_length):
        count = 0
        for cnt, item in enumerate(results, start=1):
            count = cnt
            self.assertIsNotNone(item['title'])
            self.assertIsNotNone(item['site'])
            self.assertIsNotNone(item['url'])
        self.assertEqual(count, expected_length)

    def test_item_without_author(self):
        response = self.spider.parse(self.fake_response)
        item = self._nth(response, 0)
        self.assertEqual(item, self.spider_item)

    def test_item_with_author(self):
        response = self.spider.parse(self.fake_response)
        item = self._nth(response, 1)
        self.spider_item['author'] = 'test'
        self.assertEqual(item, self.spider_item)

    def test_parse(self):
        response = self.spider.parse(self.fake_response)
        self._test_item_results(response, 30)
