# -*- coding: utf-8 -*-
import scrapy
import pandas as pd
class FirstSpider(scrapy.Spider):
	name = 'first'
	def start_requests(self):
			urls = ['https://www.worldometers.info/coronavirus/#countries']
			for url in urls:
				yield scrapy.Request(url=url, callback=self.parse)
	def parse(self, response):
		table =   pd.read_html(response.text)
		print(table)
		



