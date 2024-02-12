Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import json
... import random
... import urllib.request
... 
... # Server API URLs
... QUERY = "http://localhost:8080/query?id={}"
... 
... # 500 server request
... N = 500
... 
... 
... def getDataPoint(quote):
...     """ Produce all the needed values to generate a datapoint """
...     """ ------------- Update this function ------------- """
...     stock = quote['stock']
...     bid_price = float(quote['top_bid']['price'])
...     ask_price = float(quote['top_ask']['price'])
...     price = (bid_price+ask_price) / 2
...     return stock, bid_price, ask_price, price
... 
... 
... def getRatio(price_a, price_b):
...     """ Get ratio of price_a and price_b """
...     """ ------------- Update this function ------------- """
...     if (price_b == 0):
...         return
...     return price_a/price_b
...     
... 
... 
... # Main
... if __name__ == "__main__":
...     # Query the price once every N seconds.
...     for _ in iter(range(N)):
...         quotes = json.loads(urllib.request.urlopen(QUERY.format(random.random())).read())
... 
...         """ ----------- Update to get the ratio --------------- """
...         prices = {}
...         for quote in quotes:
...             stock, bid_price, ask_price, price = getDataPoint(quote)
...             prices[stock] = price
...             print("Quoted %s at (bid:%s, ask:%s, price:%s)" % (stock, bid_price, ask_price, price))
... 
