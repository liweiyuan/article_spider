# -*- coding: utf-8 -*-
import scrapy


class JobboleSpider(scrapy.Spider):
    name = 'jobbole'
    allowed_domains = ['blog.jobbole.com']
    start_urls = ['http://blog.jobbole.com/10287/']

    def parse(self, response):
        # //*[@id="post-94182"]/div[1]/h1
        re_selector = response.xpath('//*[@id="post-10287"]/div[1]/h1/text()')
        re2_selector = response.xpath('//*[@class="entry-header"]/h1/text()').extract()[0]
        create_data=response.xpath('//p[@class="entry-meta-hide-on-mobile"]/text()').extract()[0].strip().replace("·","").strip()
        vote=response.xpath("//span[contains(@class,'vote-post-up')]/h10/text()").extract()
        pass
