#%%
import re
# %%
# text = "a"
# pattern = "."

# text = "@"
# pattern = "."

# text = "1"
# pattern = "."

# text = "text1234124#🥳🥳🥳🥳     "
# pattern = "...."

# text = "text1234124#🥳🥳🥳🥳\n\n\n\n"
# pattern = "...."

# text = "text1234124#🥳🥳🥳🥳    ...."
# pattern = "...."

# text = "text1234124#🥳🥳🥳🥳    ...."
# pattern = "\.\.\.\."

# text = "text1234124#🥳🥳🥳🥳    ...."
# pattern = "\. \^ \$ \* \+ \? \\ \| \[ \]"

text = "text1234124#🥳🥳🥳🥳    ...."
pattern = ". ^ $ * + ? \ | [] () {}"

regex = re.compile(pattern)
all_matches = regex.findall(text)
print(all_matches)