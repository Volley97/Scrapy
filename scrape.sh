#!/usr/bin/env bash

mkdir out
scrapy crawl hrforecast_spider -o out/hrforecast.csv &
scrapy crawl gazpromvacancy_spider -o out/gazpromvacancy.csv