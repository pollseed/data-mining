import matplotlib.pylab as pl
from sklearn.datasets import load_digits
from sklearn.datasets import load_sample_image

def load_digits_test():
	digits = load_digits()
	pl.matshow(digits.images[0])
	pl.show()

def load_image_test():
	flower = load_sample_image('flower.jpg')
	pl.imshow(flower)
	pl.show()

if __name__ == '__main__':
				load_digits_test()
				load_image_test()
