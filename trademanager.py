import datetime

class portfolio:
	def __init__(self, cryptobalance, eurbalance, totalbalance):
		self.cryptobalance = cryptobalance
		self.eurbalance = eurbalance
		self.totalbalance = totalbalance

btcwallet = portfolio(1.0, 4000.0, 0)

def buybtc(price):
	if btcwallet.eurbalance > 0:
		amount = (btcwallet.eurbalance * 0.998) / price
		btcwallet.cryptobalance += amount
		print "Bought", amount, "BTC for", (btcwallet.eurbalance * 0.998), "EUR."
		amountstr = str(amount)
		euramountstr = str(btcwallet.eurbalance * 0.998)
		btcwallet.eurbalance = 0
		print "Current portfolio status:"
		print "BTC:", btcwallet.cryptobalance
		print "EUR:", btcwallet.eurbalance
		btcwallet.totalbalance = price * btcwallet.cryptobalance + btcwallet.eurbalance
		valuestr = str(btcwallet.totalbalance)
		print "Total BTC portfolio value:", btcwallet.totalbalance, "eur."
		file = open("trades.txt", "a")
		file.write(datetime.datetime.now().ctime())
		file.write("|B|%s|%s|%s.\n" % (amountstr, euramountstr, valuestr))
		file.close() 
	else:
		print "Not enough money to make a buy."

def sellbtc(price):
	if btcwallet.cryptobalance > 0:
		amount = btcwallet.cryptobalance * price
		btcwallet.eurbalance += (amount * 0.998)
		print "Sold", btcwallet.cryptobalance, "BTC for", (amount * 0.998), "EUR."
		amountstr = str(amount * 0.998)
		btcamountstr = str(btcwallet.cryptobalance)
		btcwallet.cryptobalance = 0
		print "Current portfolio status:"
		print "BTC:", btcwallet.cryptobalance
		print "EUR:", btcwallet.eurbalance
		btcwallet.totalbalance = price * btcwallet.cryptobalance + btcwallet.eurbalance
		valuestr = str(btcwallet.totalbalance)
		print "Total BTC portfolio value:", btcwallet.totalbalance, "eur."
		file = open("trades.txt", "a")
		file.write(datetime.datetime.now().ctime())
		file.write("|S|%s|%s|%s\n" % (btcamountstr, amountstr, valuestr))
		file.close()
	else:
		print "No BTC to sell."
