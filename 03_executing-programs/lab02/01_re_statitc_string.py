
#%%
import re
#%%
text = "Hello, this is some text. Hello"
pattern = "Hello"

regex = re.compile(pattern)
print(regex)

match = regex.search(text)
print(match)
#%%
string = "Hello"
print(len(string))
print(string[0])
print(string[4])
#%%
print("=" * 20)
print("match methods")
print("=" * 20)
print(match.group())
print(match.start())
print(match.end())
print(match.span())


# %%
all_matches = regex.findall(text)
print(all_matches)