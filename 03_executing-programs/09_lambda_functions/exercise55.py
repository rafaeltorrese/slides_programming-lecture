first_item = lambda my_list: my_list[0]

print(first_item(["cat", "dog", "mouse"]))


#%% [markdown]
# ## Mapping with Lambda Functions
# **map** is a spcial function in python tha applies a given function to all items in a list
names = ["Magda", "Jose", "Anne"]

lenghts = []
for name in names:
    lenghts.append(len(name))

print(lenghts)
#%%
print(map(len, names))
lenghts = [*map(len, names)]
print(lenghts)
print(sum(lenghts) / len(lenghts))


# %%
