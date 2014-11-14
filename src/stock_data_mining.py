import scipy as sp
import matplotlib.pyplot as plt

# ストックデータをタブで区分けして返します.
def get_stock_data_csv():
	return sp.genfromtxt("../data/stock_test.tsv", delimiter="\t")

# 指定したストックデータから列指向で指定引数を抜き取り返します.
def get_stock_line(stock, x_number, y_number):
	return (stock[:,x_number], stock[:,y_number])

# 散布図を出力します.
def scatter(x, y):
	# 壊れてる値弾く
	x = x[~sp.isnan(x)]
	y = y[~sp.isnan(y)]

	plt.scatter(x, y)

	# TODO 固定値にして呼ぶ
	plt.title("Stock data 8/10-10/10")
	plt.xlabel("prev_closing_price")
	plt.ylabel("No.")
	plt.grid()
	plt.show()

def main():
	stock = get_stock_data_csv()
	x, y = get_stock_line(stock, 0, 2)
	scatter(x, y)

if __name__ == '__main__':
	main()
	
