# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapeWebsiteItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    website_name = scrapy.Field()
    website_url = scrapy.Field()
    desc = scrapy.Field()
    title_tag = scrapy.Field()
    pass
