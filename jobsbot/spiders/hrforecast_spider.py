from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from jobsbot.items import BrainsItemLoader,BrainItem

from datetime import datetime


class HrforecastSpider(CrawlSpider):

    name = 'hrforecast_spider'
    start_urls = ['https://www.hrforecast.de/career/']
    rules = (
        Rule(
            LinkExtractor(
                restrict_css=('#after_section_1 > div:nth-child(1)'),
                ),'parse_item'
        ),
    )

    def parse_item(self,response):
        selector = Selector(response)
        l = BrainsItemLoader(BrainItem(), selector)
        l.add_value('job_url',response.url)
        l.add_css('job_title', '.av_two_third > section:nth-child(1) > div:nth-child(1) > p:nth-child(1) > strong:nth-child(1)::text')
        l.add_xpath('job_description', '//*[@id="av_section_1"]/div/main/div/div/div[1]/section/div')
        l.add_value('crawled_date', datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        l.add_value('posted_date', None)
        l.add_value('company_name', 'HRForecast')
        return l.load_item()
