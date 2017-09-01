import time
import json
import requests
from trademanager import buybtc, sellbtc

def getPrice():
	data=requests.get('https://api.coinbase.com/v2/prices/spot?currency=EUR')
	dictData=json.loads(data.text)
	priceAsStr = dictData['data']['amount']
	price = float(priceAsStr)
	return price

def main():
	startingPrice = getPrice()
	print "Starting price is:", startingPrice
	TRIGGER = 0.005
	loop = 1
	priceChange = 0
	kierros = 0
	while loop == 1:
		print "Price change since last trade:", priceChange
		time.sleep(30)
		newPrice = getPrice()
		print "Current BTC price is:", newPrice
		if kierros == 0:
			priceChange = priceChange + newPrice - startingPrice
			kierroes = 1
		else:
			priceChange = priceChange + newPrice - newPrice2
		time.sleep(30)
		newPrice2 = getPrice()
		print "Current BTC price is:", newPrice2
		priceChange2 = newPrice2 - newPrice
		
		if (priceChange > 0 and priceChange2 > 0) or (priceChange < 0 and priceChange2 <0):
			priceChange = newPrice2 - startingPrice
		else:
			suhde = newPrice2 / startingPrice
			if suhde > 1 + TRIGGER or suhde < 1 - TRIGGER:
				if suhde < 1:
					buybtc(newPrice2)
				if suhde > 1:
					sellbtc(newPrice2)
				priceChange = 0
				startingPrice = newPrice2
			else:
				priceChange = newPrice2 - startingPrice

main()
				
