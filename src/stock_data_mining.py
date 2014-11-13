import matplotlib.pyplot as plt

stock = sp.genfromtxt("stock_test.tsv", delimiter="\t")
a = stock[:,0]
b = stock[:,2]
a = a[~sp.isnan(a)]
b = b[~sp.isnan(b)]
plt.scatter(a,b)
plt.title("Stock data 8/10-10/10")
plt.xlabel("prev_closing_price")
plt.ylabel("No.")
plt.grid()
plt.show()
