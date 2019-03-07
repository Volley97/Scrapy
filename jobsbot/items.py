from scrapy.loader import ItemLoader
import scrapy
from scrapy.loader.processors import TakeFirst, Join, MapCompose
from w3lib.html import remove_tags


class BrainItem(scrapy.Item):
    job_title = scrapy.Field()
    company_name = scrapy.Field()
    job_description = scrapy.Field()
    crawled_date = scrapy.Field()
    posted_date = scrapy.Field()
    job_url = scrapy.Field()


def format_description(x):
    return x.replace('\r', '').replace('\n', ' ').replace('  ', ' ').strip()


class BrainsItemLoader(ItemLoader):
    url_out = TakeFirst()
    job_title_out = TakeFirst()
    job_description_in = MapCompose(remove_tags, format_description)
    job_description_out = Join()
    company_name_out = TakeFirst()
    date_of_public_out = TakeFirst()
