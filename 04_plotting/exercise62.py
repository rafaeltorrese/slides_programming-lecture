import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns



temperature = np.loadtxt(r"04_plotting\data\temperature.txt", dtype=float)
sales = np.loadtxt(r"04_plotting\data\sales.txt", dtype=float)



plt.title('Ice-cream sales versus temperature')
plt.xlabel('Sales')
plt.ylabel('Temperature')
plt.scatter(temperature, sales, color="red")
plt.show()

calendars = np.loadtxt('04_plotting/data/calendars.txt')
print(calendars.mean())
print(calendars[2000:].mean())
cum_avg = calendars.cumsum() / np.arange(1, calendars.size + 1) 
plt.plot(cum_avg)
plt.axhline(cum_avg[-1], color="red")
plt.axvline(2000, lw=3, color='blue')
plt.show()