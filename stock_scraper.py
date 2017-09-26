from urllib2 import urlopen
from bs4 import BeautifulSoup

import csv
from datetime import datetime

import shutil




# Scrape the webpage
def scraper(pages):
	datestring = datetime.strftime(datetime.now(), '%Y%m%d_%H%M%S')
	data = []
	
	page = urlopen(pages)
	
	#parse the html using beautiful soup and store in variable 'soup'
	soup = BeautifulSoup(page, 'html.parser')
	
	#take out the <div> of name and get its value
	name_box = soup.find('h1', attrs={'class': 'name'})
	stock_name = name_box.text.strip()
	
	#get the index price
	price_box = soup.find('div', attrs={'class': 'price'})
	stock_price = price_box.text
	
	#get the opening priced
	opening_box = soup.find_all('div', attrs={'class': 'cell__value cell__value_'})[0]
	stock_opening = opening_box.text
	
	#get the volume
	volume_box = soup.find_all('div', attrs={'class': 'cell__value cell__value_'})[7]
	stock_volume = volume_box.text
		
	stock_info = [stock_name, stock_price, stock_opening, stock_volume, datestring]

			
	return stock_info
