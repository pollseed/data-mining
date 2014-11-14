import scipy as sp
import matplotlib.pyplot as plt

def get_stock_data_csv():
	# 株情報8/10〜10/10までのやつを取得して分布させてみる
	return sp.genfromtxt("../data/stock_test.tsv", delimiter="\t")

def conpare(x, y):
	# 壊れてる値弾く
	x = x[~sp.isnan(x)]
	y = y[~sp.isnan(y)]

	# 分布図で行こうと思う
	plt.scatter(x, y)

	# TODO 固定値にして呼ぶ
	plt.title("Stock data 8/10-10/10")
	plt.xlabel("prev_closing_price")
	plt.ylabel("No.")
	plt.grid()
	plt.show()

def main():
	stock = get_stock_data_csv()
	conpare(stock[:,0], stock[:,2])

if __name__ == '__main__':
	main()
