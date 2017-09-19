

#import libraries
import urllib2
from bs4 import BeautifulSoup

import csv
from datetime import datetime

def scraper():
	# specify the url
	quote_page = ['https://www.bloomberg.com/quote/MSFT:US', 'https://www.bloomberg.com/quote/WMT:US', 'https://www.bloomberg.com/quote/VZ:US']

	#open a csv file with append, so old data will not be erased
	datestring = datetime.strftime(datetime.now(), '%Y%m%d_%H%M%S')

	#with open('index_'+ datestring +'.csv', 'a') as csv_file:
		#writer = csv.writer(csv_file)
		#writer.writerow(['Name', 'Price', 'Opening', 'Volume', 'Date & Time'])

	#for loop
	data = []
	for pg in quote_page:
	
		#query the website and return the html to the variable 'page'
		page = urllib2.urlopen(pg)
	
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
	
		#save the data in a tuple
		#data.append((stock_name, stock_price, stock_opening, stock_volume))
			
		#with open('index_'+ datestring + '.csv', 'ab') as csv_file:
			#writer = csv.writer(csv_file)
			#writer.writerow([name, price, opening, volume, datetime.now()])
			
	return stock_info
