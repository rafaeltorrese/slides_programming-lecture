#%% [markdown]
# ##Exercise 56
# In this exercise, you use map with a lambda function to apply the logistic function to a list of values
# \[ f(x) = \frac{1}{1 + e^{-x} }\]
import math
# %%
nums = [-3, -5, 1, 4]
#%%
print(list(map(lambda x: 1 / (1 + math.exp(-x)), nums)))
logistic = lambda x: 1 / (1 + math.exp(-x))
print([logistic(number) for number in nums] )
