# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import psycopg2


class Pipeline(object):

    def open_spider(self, spider):
        hostname = 'localhost'
        username = 'jobsbot_user'
        password = 'jobsbot_pwd'
        database = 'jobsbot'
        self.connection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
        self.cur = self.connection.cursor()

    def close_spider(self, spider):
        self.cur.close()
        self.connection.close()

    def process_item(self, item, spider):
        self.cur.execute("insert into jobs(job_title,job_url,job_description,company_name,crawled_date,posted_date) values(%s,%s,%s,%s,%s,%s)", (item.get('job_title'), item['job_url'], item.get('job_description'), item.get('company_name'), item['crawled_date'], item.get('posted_date')))
        self.connection.commit()
        return item
