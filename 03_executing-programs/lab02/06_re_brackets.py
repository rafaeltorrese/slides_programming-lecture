#%%
import re
# %%
text = ""
pattern = ""

regex = re.compile(pattern)
all_matches = regex.findall(text)
print(all_matches)