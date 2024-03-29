# -*- coding: utf-8 -*-
import scrapy
import sqlite3 
from ..items import AmazonItem


class AmazonSpiderSpider(scrapy.Spider):
	page_num = 2
	name = 'amazon'
	start_urls = [ 'https://www.amazon.in/s?k=laptops&ref=nb_sb_noss_2']

	def parse(self, response):
		item = AmazonItem()
		product_name = response.css('.a-color-base.a-text-normal::text').extract()
		product_price = response.css('.sg-col-20-of-28 .a-price-whole').css('::text').extract()
		product_imagelink = response.css('.s-image::attr(src)').extract()
		item['product_name'] = product_name
		item['product_price'] = product_price
		item['product_imagelink'] = product_imagelink
		yield item

		next_page = 'https://www.amazon.in/s?k=laptops&page=' + str(AmazonSpiderSpider.page_num) + '&qid=1590928418&ref=sr_pg_2'
		if AmazonSpiderSpider.page_num<=20:
			AmazonSpiderSpider.page_num += 1
			yield response.follow(next_page,callback = self.parse)
