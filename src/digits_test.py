import matplotlib.pylab as pl
from sklearn.datasets import load_digits

def load():
	digits = load_digits()
	pl.matshow(digits.images[0])
	pl.show()

if __name__ == '__main__':
				load()
