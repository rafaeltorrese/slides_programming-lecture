#%% [markdown]
# # Exercise 63: 
# Drawing a Line Chart to Find the Growth in Stock Prices In this exercise, you will be plotting the stock prices of a well-known company. You will be plotting this as a line chart that will be plotted as the number of days against the growth in price.
#%%
import numpy as np
import matplotlib.pyplot as plt
#%%
calendars = np.loadtxt("data/calendars.txt", dtype=float)
stock_price = np.loadtxt(r".\data\stock.txt", dtype=float)
cumavg = calendars.cumsum() / np.arange(1, len(calendars) + 1)
print(stock_price)
#%%
plt.title('Opening Sotck Prices')
plt.xlabel('Days')
plt.ylabel('$ USD')

plt.plot(stock_price)

plt.show()
# %%
