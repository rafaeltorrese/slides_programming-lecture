#%%
import re
# %%
# text = "123"
# pattern = "123"

# text = "123123"
# pattern = "123"

# text = "1 23123"
# pattern = "\d \d\d"

# text = "123 cat dog 456"
# pattern = "\d\d\d"

# text = "123 cat dog 456"
# pattern = "\D\D\D"

text = "123 cat dog 456"
pattern = "\D\D\D"
regex = re.compile(pattern)

# %%
all_matches = regex.findall(text)
print(all_matches)
# %%
