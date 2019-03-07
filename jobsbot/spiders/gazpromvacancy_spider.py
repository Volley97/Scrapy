from datetime import datetime

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from jobsbot.items import BrainsItemLoader,BrainItem

class GazpromvacancySpider(CrawlSpider):
    name = 'gazpromvacancy_spider'
    start_urls = ['https://www.gazpromvacancy.ru/jobs/']
    rules = (
        Rule(
            LinkExtractor(
                restrict_css=('.job-list-container')
                ),'parse_item'
        ),
    )
    def parse_item(self,response):
        selector = Selector(response)
        l = BrainsItemLoader(BrainItem(), selector)
        l.add_value('job_url',response.url)
        l.add_css('job_title','.job-title::text')
        l.add_css('company_name','.job-params > dd:nth-child(2) > a:nth-child(1)::text')
        l.add_value('crawled_date', datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        l.add_css('posted_date','.job-params > dd:nth-child(10) > time:nth-child(1)::text')
        l.add_xpath('job_description', '//*[@id="content-normal"]')

        return l.load_item()
