import re

text = "век, веко, вектор, верификация"
match = re.findall('век', text)

print(match)