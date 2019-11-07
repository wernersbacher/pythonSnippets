import time


class TicToc:
	"""
		simple time keeper.
		measures time between two points in the code.

		set start to False if you want to trigger the start signal manually.

	"""
	def __init__(self, start=True):
		self.start = 0
		self.end = 0
		self.length = 0

		if start:
			self.tic()

	def tic(self):
		self.start = time.time()

	def toc(self):
		self.end = time.time()
		self.length = self.end - self.start

		return self.length



if __name__ == "__main__":

	timer = TicToc() # automatically starts on init

	for i in range(20000):
		x = 2 ** i

	print("Time elapsed: {:.4f} seconds".format(timer.toc())) # .toc ends measurement and return the value
