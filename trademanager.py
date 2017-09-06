import datetime

class portfolio:
	def __init__(self, cryptobalance, eurbalance):
		self.cryptobalance = cryptobalance
		self.eurbalance = eurbalance

btcwallet = portfolio(1.0, 4000.0)

def buybtc(price):
	if btcwallet.eurbalance > 0:
		amount = btcwallet.eurbalance / price
		btcwallet.cryptobalance += amount
		print "Bought", amount, "BTC for", btcwallet.eurbalance, "EUR."
		amountstr = str(amount)
		euramountstr = str(btcwallet.eurbalance)
		btcwallet.eurbalance = 0
		print "Current portfolio status:"
		print "BTC:", btcwallet.cryptobalance
		print "EUR:", btcwallet.eurbalance
		file = open("trades.txt", "a")
		file.write(datetime.datetime.now().ctime())
		file.write(" BUY %s btc for %s eur.\n" % (amountstr, euramountstr))
		file.close() 
	else:
		print "Not enough money to make a buy."

def sellbtc(price):
	if btcwallet.cryptobalance > 0:
		amount = btcwallet.cryptobalance * price
		btcwallet.eurbalance += amount
		print "Sold", btcwallet.cryptobalance, "BTC for", amount, "EUR."
		amountstr = str(amount)
		btcamountstr = str(btcwallet.cryptobalance)
		btcwallet.cryptobalance = 0
		print "Current portfolio status:"
		print "BTC:", btcwallet.cryptobalance
		print "EUR:", btcwallet.eurbalance
		file = open("trades.txt", "a")
		file.write(datetime.datetime.now().ctime())
		file.write(" SELL %s btc for %s eur.\n" % (btcamountstr, amountstr))
		file.close()
	else:
		print "No BTC to sell."
