import re

text = "век, веко, вектор"
match = re.findall('век', text)

print(match)