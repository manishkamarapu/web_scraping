import scrapy
from scrape_website.items import ScrapeWebsiteItem


class ScrapySpider(scrapy.Spider):
    name = "posts"
    start_urls = [
        'http://dmoztools.net/Business/Education_and_Training/Technology/',
        'http://dmoztools.net/Business/Education_and_Training/Team_Building/'
    ]

    def parse(self, response):
        pages = response.xpath('//*[@id="site-list-content"]/div')
        items = []
        for page in pages:
            item = ScrapeWebsiteItem()
            item['website_name'] = page.xpath('div/a/div/text()').extract()[0]
            item['website_url'] = page.xpath('div/a/@href').extract()[1]
            item['desc'] = page.xpath('div/div/text()').extract()[0]
            url = page.xpath('div/a/@href').extract()[1]

            yield response.follow(url, self.parse_additional_page, cb_kwargs=dict(item=item))

    def parse_additional_page(self, response, item):
        item['title_tag'] = response.css('title::text').extract()
        return item
