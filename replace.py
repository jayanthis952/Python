import re

text = " This is my best life"
pattern = r'my'
replacement = "our"

new_text = re.sub(pattern, replacement, text)
print(new_text)
