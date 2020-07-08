import urllib.request
import json


def getStockData(stockSymbol):
    urlBase = 'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol='
    apiKeyURL = '&apikey=W0B9ZZ89KT3JSFXX'

    api_URL = urlBase + stockSymbol + apiKeyURL

    connection = urllib.request.urlopen(api_URL)
    responseString = connection.read().decode()
    return (responseString)


stockSymbol = ''
stockSymbol = input("Enter stock symbol to look up: ")

while stockSymbol != 'quit':
    stockJSON = getStockData(stockSymbol)
    print(stockJSON)

    json_dict = json.loads(stockJSON)

    priceQuote = json_dict['Global Quote']['05. price']

    printString = 'The current price of ' + stockSymbol + ' is: ' + priceQuote
    print(printString)

    stockSymbol = input("Enter stock symbol to look up: ")
