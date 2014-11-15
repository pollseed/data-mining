#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import sys, csv, datetime

# ストックデータをタブで区分けして返します.
# TODO うまく動作しない.原因は１次元配列になってしまっているから
def get_stock_data_csv():
	return sp.genfromtxt(
		"../data/stock_test.tsv",
		delimiter="\t",
		skiprows=1,
		dtype={
		'names':(
			'id',
			'announce_date',
			'prev_closing_price',
			'opening_price',
			'high_price',
			'low_price',
			'buy_flg',
			'delete_flg',
			'created',
			'updated'),
		'formats':(
			'i4', 'S10',
			'f8', 'f8', 'f8', 'f8', 'b', 'b',
			'S21', 'S21')})

def get_stock_data_csv_tmp():
	return sp.genfromtxt("../data/stock_test.tsv", delimiter="\t")

# 指定したストックデータから列指向で指定引数を抜き取り返します.
def get_stock_line(stock, x_number, y_number):
	# for x in stock[:,x_number]:
	# 	datetime.datetime(x)

	# y = stock[:,y_number]
	return (stock[:,x_number], stock[:,y_number])

# 散布図を出力します.
def scatter(x, y):
	# 壊れてる値弾く
	# x = x[~sp.isnan(x)]
	print("x軸のデータを出力します")
	print(x)
	# y = y[~sp.isnan(y)]
	print("y軸のデータを出力します")
	print(y)

	plt.scatter(x, y)

	# TODO 固定値にして呼ぶ
	plt.title("Stock data 8/10-10/10")
	plt.xlabel("prev_closing_price")
	plt.ylabel("No.")
	plt.grid()
	plt.show()

def main():
	# ストックデータを取得
	stock = get_stock_data_csv_tmp()
	# ストックデータから任意の列をもぐ
	x, y = get_stock_line(stock, 0, 3)
	# 散布図出力
	scatter(x, y)

if __name__ == '__main__':
	main()
