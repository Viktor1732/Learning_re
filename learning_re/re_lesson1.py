# import re

# text = "век, веко, вектор"
# match = re.findall(r'век', text)
#
# text = "век, Век, века"
# match = re.findall(r'[Вв]ек', text)

# text = "век, Век, века"
# match = re.findall(r'([Вв]ек)', text)

# text = "(век), Век, века"
# match = re.findall(r'\([Вв]ек\)', text)

# text = "в12ек, Ве7к, ве3ка"
# match = re.findall('[0123456789][0123456789]', text)

# text = "в12ек, Ве7к, ве3ка"
# match = re.findall('[0-9][0-9]', text)

# text = "в12ек, Ве-7к, ве3ка"
# match = re.findall('[-0-9][0-9]', text)

# text = "в12ек, Ве7к, ве3ка"
# match = re.findall('[^0-9]', text)

# text = "в12ек, Ве7к, ве3ка"
# match = re.findall('[а-яА-Я]', text)

# text = "в12ек, Ве7к, ве3ка"
# match = re.findall('[а-яА-Я]', text)

# . - лубой символ
# \d - любая цифра
# \D - любая не цира
# \s - любой пробельный символ(\t\n\f\r\v)
# \S - любой не пробельный символ
# \w - любой символ слова. При флаге re.ASCII набору символов [a-zA-Z0-9]
# \W - любой не символ слова. При флаге re.ASCII набору символов [^a-zA-Z0-9]

# text = "в12ек, Ве7к, ве3ка"
# match = re.findall(r'\d', text)

# text = "в12ек, Ве7к, ве3ка"
# match = re.findall(r'\S', text)

# text = "в12ек, Ве7к, ве3ка"
# match = re.findall(r'\w', text, re.ASCII)

# text = "0xf, 0xa, 0x5"
# match = re.findall(r"0x[\da-fA-F]", text)


# print(match)
