import re
str = "I Will get good work from home job with good package in infosys"
pattern = r'package'
match = re.search(pattern,str)
if match:
    print("The match found",match.group())
else:
    print("No match found")


# import re

# text = "The quick brown fox"
# pattern = r"quick"

# match = re.search(pattern, text)
# if match:
#     print("Match found:", match.group())
# else:
#     print("No match")