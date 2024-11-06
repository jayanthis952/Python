import re

text = "banana,grapes,orange,pineapple,apple"
pattern = r','
new_text = re.split(pattern,text)
print(new_text)
