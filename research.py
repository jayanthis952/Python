import re

text = "The quick brown colour"
pattern = r'brown'
search = re.search(pattern,text)

if search:
    print("Found")
else:
    print("Not found")