#%% [markdown]
# # Exercise 63: 
# Drawing a Line Chart to Find the Growth in Stock Prices In this exercise, you will be plotting the stock prices of a well-known company. You will be plotting this as a line chart that will be plotted as the number of days against the growth in price.
#%%
import numpy as np
import matplotlib.pyplot as plt
#%%
stock_price = np.loadtxt(r".\data\stock.txt", dtype=float)

print(stock_price)
#%%
plt.plot(stock_price)

plt.show()
# %%
