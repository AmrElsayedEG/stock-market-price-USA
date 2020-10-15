import requests

def get_price_list_daily(symbol,key): #Connect with API and get Daily prices for one symbol
   r = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=%s&apikey=%s' % (symbol,key))
   price = r.json() #Convert to JSON
   price_list = price["Time Series (Daily)"] #Get the Values for "Time Series (Daily)" Key in the dict from JSON
   price_data = [] #list to hold the date & Low & Open & Close & High prices
   #Note, The Addon that makes charts takes prices in a list with the following order
   for k, v in price_list.items():
       price_data.append([str(k), float(v['3. low']),float(v['1. open']),float(v['4. close']), float(v['2. high'])])
   return price_data


import pandas #Import Pandas to read from CSV
import os
#Note: The csv file downloaded from API End-point https://www.alphavantage.co/query?function=LISTING_STATUS&apikey=demo
file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'list.csv') #Open CSV File that contains all the stock market symbols
def get_symbol():
        file = pandas.read_csv(file_path)
        symbol_list = file.loc[:, 'symbol'] #Get Symbol column only
        return symbol_list
