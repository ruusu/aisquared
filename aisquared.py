import time
import json
import requests
from trademanager import buybtc, sellbtc
import os

def getPrice():
	data=requests.get('https://api.coinbase.com/v2/prices/spot?currency=EUR')
	dictData=json.loads(data.text)
	priceAsStr = dictData['data']['amount']
	price = float(priceAsStr)
	return price

def main():
	if not os.path.isfile("price.txt"):
		file = open("price.txt", "w")
		file.close()
	if not os.path.isfile("trades.txt"):
		file = open("trades.txt", "w")
		file.close()
	startingPrice = getPrice()
	if os.path.getsize("price.txt") == 0:
		file = open("price.txt", "w")
		priceStr = str(startingPrice)
		file.write("%s" % priceStr)
		print "First run detected, price.txt initialized."
	else:
		file = open("price.txt", "r")
		priceStr = file.readline()
		startingPrice = float(priceStr)
	print "Starting price is:", startingPrice
	TRIGGER = 0.005
	loop = 1
	priceChange = 0
	kierros = 0
	while loop == 1:
		if kierros == 1:
			print "Price change since last trade:", priceChange
		time.sleep(30)
		newPrice = getPrice()
		print "Current BTC price is:", newPrice
		if kierros == 0:
			priceChange = priceChange + newPrice - startingPrice
			kierros = 1
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
				priceStr = str(startingPrice)
				file = open("price.txt", "w")
				file.write("%s" % priceStr)
				file.close()
			else:
				priceChange = newPrice2 - startingPrice

main()
				
