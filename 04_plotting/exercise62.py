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