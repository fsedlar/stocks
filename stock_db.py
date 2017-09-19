
import psycopg2
import sys

from psycopg2.extensions import AsIs
#current_table = 'stock_values_3'


#import scraper function
from stock_scraper import scraper 

#connect to the postres db
conn_string = "host='localhost' dbname='stocks' user='frank' password='B00tl3gged'"

conn = psycopg2.connect(conn_string)
print "Opened databse successfully"

#create a table in the postres db
cur = conn.cursor()
cur.execute('CREATE TABLE stock_values_6(ID serial PRIMARY KEY, Name VARCHAR(40), Price VARCHAR(40), Opening VARCHAR(40), Volume VARCHAR(40), DT VARCHAR(40))')


print "Table created successfully"

stock_info = scraper()

SQL = '''INSERT INTO stock_values_6 (ID, Name, Price, Opening, Volume, DT) VALUES (%s, %s, %s, %s, %s, %s)'''
data = (1, stock_info[0], stock_info[1], stock_info[2], stock_info[3], stock_info[4])

cur.execute(SQL, data)

#cur.execute('INSERT INTO stock_values_6(ID, Name, Price, Opening, Volume, DT) VALUES (1, stock_stuff[0], stock_stuff[1], stock_stuff[2], stock_stuff[3], stock_stuff[4])')

conn.commit()
print "Records created successfully"
conn.close()




