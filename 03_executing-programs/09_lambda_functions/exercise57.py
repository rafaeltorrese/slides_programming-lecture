# %% [markdown]
# ## Filtering with Lambda Functions
# he filter is another special function that, like map, takes a function and iterables (for example, a list) as inputs. It returns the elements for which the function returns True

names = ["Karen", "Jim", "Kim"]
print([*filter(lambda name: len(name) == 3, names)])
#%% [markdown]
# ## Exercise 57 Using the Filter Lambda
nums = [*range(1000)]

filtered = filter(lambda x: x % 3 == 0 or x % 7 == 0, nums)
print(sum(filtered))

#%% [markdown]
# Sorting with Lambda Functions
# suppose that you had a list of names, and wanted them sorted by length:
names = ["Ming", "Jennifer", "Andrew", "Boris"]
print(sorted(names))
print(sorted(names, key=lambda x: len(x)))
print(sorted(names, key=lambda x: len(x), reverse=True))


ages = [("Carmen", 50), ("Edgar", 45), ("Mario", 49), ("Joaquin", 58)]

print(min(ages, key=lambda x:x[1]))

print(help(ages.sort))