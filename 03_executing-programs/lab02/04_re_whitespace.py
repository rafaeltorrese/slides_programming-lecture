#%%
import re
# %%

# print(". .")
# print(".     .")
# print(".\t.")
# print(".\n.")


# text = "First line."
# pattern = "\s"

# text = "First  line."
# pattern = "\s"

# text = "First  line."
# pattern = "\s\s"

# text = "First line.\n"
# pattern = "\s"

# text = """First line.
# Second
# Third"""
# pattern = "\s"

# text = "First line.\nSecond line."
# pattern = "\s"

# text = "First line.\nSecond\tline."
# pattern = "\s"

# text = "First line.\nSecond\tline."
# pattern = "\s\s\s\s"

# text = "First line.\n\n\n\nSecond\tline."
# pattern = "\s\s\s\s"

text = "First line.\n\n\n\nSecond\tline."
pattern = "\S\S\S\S\S"

regex = re.compile(pattern)
all_matches = regex.findall(text)
print(all_matches)

# %%
