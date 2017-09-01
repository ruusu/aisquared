class portfolio:
	def __init__(self, cryptobalance, eurbalance):
		self.cryptobalance = cryptobalance
		self.eurbalance = eurbalance

btcwallet = portfolio(1.0, 4000.0)

def buybtc(price):
	amount = btcwallet.eurbalance / price
	btcwallet.cryptobalance += amount
	print "Bought", amount, "BTC for", btcwallet.eurbalance, "EUR."
	btcwallet.eurbalance = 0
	print "Current portfolio status:"
	print "BTC:", btcwallet.cryptobalance
	print "EUR:", btcwallet.eurbalance

def sellbtc(price):
	amount = btcwallet.cryptobalance * price
	btcwallet.eurbalance += amount
	print "Sold", btcwallet.cryptobalance, "BTC for", amount, "EUR."
	btcwallet.cryptobalance = 0
	print "Current portfolio status:"
	print "BTC:", btcwallet.cryptobalance
	print "EUR:", btcwallet.eurbalance
