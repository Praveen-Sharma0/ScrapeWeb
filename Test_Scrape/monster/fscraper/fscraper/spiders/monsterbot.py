# -*- coding: utf-8 -*-
import scrapy


class MonsterbotSpider(scrapy.Spider):
    name = 'monsterbot'
    allowed_domains = ['https://www.monsterindia.com/front-end-developer-jobs-in-bengaluru-bangalore.html']
    start_urls = ['https://www.monsterindia.com/front-end-developer-jobs-in-bengaluru-bangalore.html/']

    def parse(self, response):
        
        #Extracting the content using css selectors
        company_name=response.css(".jtxt.orange span::text").extract()
        skills = response.css('.jtxt::attr(title)').extract()
        location  = response.css(".ico1 span::text").extract()
        experience = response.css(".ico2 span::text").extract()

        #Give the extracted content row wise
        for item in zip(company_name,skills,location,experience):

            scraped_info = {
                'Company Name' :item[0],
                'Skills':item[1],
                'Location' : item[2],
                'Experience':item[3],
            }
            #yield or give the scraped info to scrapy
            yield scraped_info
        #pass
