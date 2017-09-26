
import psycopg2
import sys
from urllib2 import urlopen
import shutil

from psycopg2.extensions import AsIs


#import scraper function
from stock_scraper import scraper 


## Set up a postgres table
#connect to the postres db
conn_string = "host='localhost' dbname='stocks' user='frank' password='B00tl3gged'"

conn = psycopg2.connect(conn_string)
print "Opened databse successfully"

#create a table in the postres db
cur = conn.cursor()
cur.execute('CREATE TABLE stock_values(ID serial PRIMARY KEY, Name VARCHAR(40), Price VARCHAR(40), Opening VARCHAR(40), Volume VARCHAR(40), DT VARCHAR(40))')


print "Table created successfully"


## Insert data for each stock into the table
urls = ['https://www.bloomberg.com/quote/MSFT:US', 'https://www.bloomberg.com/quote/WMT:US', 'https://www.bloomberg.com/quote/VZ:US', 'https://www.bloomberg.com/quote/ACM:US', 'https://www.bloomberg.com/quote/TWTR:US','https://www.bloomberg.com/quote/TWLO:US']

for url in urls:
	stock_info = scraper(url)

	SQL = '''INSERT INTO stock_values (Name, Price, Opening, Volume, DT) VALUES (%s, %s, %s, %s, %s)'''
	data = (stock_info[0], stock_info[1], stock_info[2], stock_info[3], stock_info[4])

	cur.execute(SQL, data)



conn.commit()
print "Records created successfully"
conn.close()




