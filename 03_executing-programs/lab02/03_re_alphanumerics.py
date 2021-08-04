#%%
import re
# %% [markdown]
# # Alphanumerics

# text = "1aA"
# pattern = "\w"

# text = "1aA $"
# pattern = "\w"

# text = "123 cat dog 456"
# pattern = "\w"

# text = "123 cat dog 456"
# pattern = "\w\w\w"

# text = "123 cat dog 456 !@#"
# pattern = "\w\w\w"

text = "123 cat dog 456 !@#"
pattern = "\W\W\W"

regex = re.compile(pattern)
# %%
all_matches = regex.findall(text)
print(all_matches)