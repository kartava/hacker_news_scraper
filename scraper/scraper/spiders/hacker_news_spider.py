import urlparse

import scrapy
from scrapy.exceptions import CloseSpider

from scraper.items import SpiderItem


class HackerNewsSpider(scrapy.Spider):
    name = "news"
    allowed_domains = ['news.ycombinator.com']
    start_urls = (
        'https://news.ycombinator.com/',
    )

    def __init__(self, page_count=None, *args, **kwargs):
        self.page_count = page_count
        self.max_page_count = 100
        super(HackerNewsSpider, self).__init__(*args, **kwargs)

    @staticmethod
    def extractor(row, path):
        return row.css(path).extract_first()

    def parse(self, response):

        rows = response.xpath('//tr[@class="athing"]')
        for row in rows:
            site_url = self.extractor(row, 'span.sitebit.comhead>a::attr(href)')
            kwargs = {
                'title': self.extractor(row, 'a.storylink::text'),
                'author': self.extractor(row, 'tr + tr a.hnuser::text'),
                'url': self.extractor(row, 'a.storylink::attr(href)'),
                'site': '{}{}'.format(response.url, site_url or '')
            }
            yield SpiderItem(**kwargs)

        next_page = response.xpath('//a[@class="morelink"]/@href').extract_first()
        if next_page and self.page_count is not None:
            url_params = urlparse.urlparse(next_page)
            next_page_id = int(url_params.query.replace('p=', ''))
            if next_page_id > int(self.page_count) or next_page_id > self.max_page_count:
                raise CloseSpider(reason='Maximum depth exceeded')
            yield scrapy.Request(response.urljoin(next_page), callback=self.parse)
