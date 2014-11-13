import matplotlib.pyplot as plt

# 株情報8/10〜10/10までのやつを取得して分布させてみる
stock = sp.genfromtxt("../data/stock_test.tsv", delimiter="\t")
a = stock[:,0]

# とりあえず終値だけ取得させる
b = stock[:,2]

# 壊れてる値弾く
a = a[~sp.isnan(a)]
b = b[~sp.isnan(b)]

# 分布図で行こうと思う
plt.scatter(a,b)
plt.title("Stock data 8/10-10/10")
plt.xlabel("prev_closing_price")
plt.ylabel("No.")
plt.grid()
plt.show()
