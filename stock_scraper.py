# import libraries
import urllib2
from bs4 import BeautifulSoup

import csv
from datetime import datetime

# specify the url
quote_page = ['https://www.bloomberg.com/quote/SPX:IND', 'https://www.bloomberg.com/quote/CCMP:IND']

# for loop
data = []
for pg in quote_page:
	#query the website and return the html to the variable 'page'
	page = urllib2.urlopen(pg)
	
	#parse the html using beautiful soup and store in variable 'soup'
	soup = BeautifulSoup(page, 'html.parser')
	
	#take out the <div> of name and get its value
	name_box = soup.find('h1', attrs={'class': 'name'})
	name = name_box.text.strip()
	
	#get the index price
	price_box = soup.find('div', attrs={'class': 'price'})
	price = price_box.text
	
	#save the data in a tuple
	data.append((name, price))
	
	#open a csv file with append, so old data will not be erased
	with open('index.csv', 'a') as csv_file:
		writer = csv.writer(csv_file)
		#the for loop
		for name, price in data:
			writer.writerow([name, price, datetime.now()])



#query the website and return the html to the variable 'page'
#page = urllib2.urlopen(quote_page)

#parse the html using beautiful soup and store in variable 'soup'
#soup = BeautifulSoup(page, 'html.parser')

#take out the <div> of name and get its value
#name_box = soup.find('h1', attrs = {'class': 'name'})

#name = name_box.text.strip() #strip is used to remove starting and trailing

#print name

#get the index price
#price_box = soup.find('div', attrs = {'class': 'price'})
#price = price_box.text
#print price

#open a csv file with append, so old data will not be erased
#with open ('index.csv', 'a') as csv_file:
#	writer = csv.writer(csv_file)
#	writer.writerow([name, price, datetime.now()])