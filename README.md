# Scrapy

Parsed attributes
job_title, company_name, crawled_date, posted_date, job_description and job_url.

Prerequisites

virtualven venv
pip install -r requirements.txt
source venv/bin/activate

Setup db

Install Postgres with http://www.postgresqltutorial.com/install-postgresql/
launch psql and run "\i create_db_schema.sql"

How to start a spider

mkdir out
scrapy crawl hrforecast_spider -o out/hrforecasr.csv
scrapy crawl gazpromvacancy_spider -o out/gazpromvacancy.csv

How to start both spiders
chmod +x scrape.sh
./scrape.sh

Check db

Launch psql
\connect jobsbot
select job_title, job_url, posted_date, crawled_date, company_name from jobs;
