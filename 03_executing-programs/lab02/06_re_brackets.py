#%%
import re
# %%
# text = ""
# pattern = "\d[yt]"

# text = "24"
# pattern = "\d[0123456789]"

# text = "24"
# pattern = "[0123456789]"

# text = "24"
# pattern = "[01234asdf56789]"

# text = "I am groot. You are you"
# pattern = "[aeiou]"

# text = "I am groot. You are you"
# pattern = "[aeiou][aeiou]"

# text = "I am groot. You are you"
# pattern = "[0-9]\d"

# text = "I am groot. You are you"
# pattern = "[^0-9] \D"

# text = "I am groot. You are you"
# pattern = "[^asdflkj]"

# text = "I am groot. You are you"
# pattern = "[A-Z]"

# text = "I am groot. You are you"
# pattern = "[a-z]"

# text = "I am groot. You are you"
# pattern = "[A-Za-z]"

# text = "I am groot. You are you"
# pattern = "[A-Za-d]"

text = "I am groot. You are you"
pattern = "[A-Zabcd]"


regex = re.compile(pattern)
all_matches = regex.findall(text)
print(all_matches)