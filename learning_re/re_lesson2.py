import re

# #Мажорный квантификатор
# text = "Google, Gooogle, Goooooogle"
# match = re.findall(r"o{2,5}?", text)

# Минорный квантификатор
# text = "Google, Gooogle, Goooooogle"
# match = re.findall(r"o{2,5}?", text)

# text = "Google, Gooogle, Goooooogle"
# match = re.findall(r"Go{3,}gle", text)

# text = "Google, Gooogle, Goooooogle"
# match = re.findall(r"Go{,4}gle", text)

# phone = '89080197684'
# match = re.findall(r"8\d{10}", phone)

# ? - от ноля до одного (аналог {0,1});
# * - от ноля до бесконечности (аналог {0,})
# + - от единицы до бесконечности (аналог {1,})

# text = "стекляный, стеклянный"
# match = re.findall(r"стеклянн?ый", text)

# text = "author = Пушкин А.С.; title = Евгений Онегин; price = 200; year=2001"
# match = re.findall(r"\w+\s*=\s*[^;]+", text)
#
# text = "author = Пушкин А.С.; title = Евгений Онегин; price = 200; year=2001"
# match1 = re.findall(r"(\w+)\s*=\s*(\w[^;]+)", text)

# text = "<p>Картинка <img src='bg.jpg'>в тексте</p>"
# match = re.findall(r"<img.*?>", text)

# text = "<p>Картинка <img src='bg.jpg'>в тексте</p>"
# match = re.findall(r"<img[^>]*>", text)

text = "<p>Картинка <img src='bg.jpg'> в тексте</p>"
# match = re.findall(r"<img\s+.*?src\s*=\s*[^>]+>", text)
match = re.findall(r"<img\s+[^>]*?src\s*=\s*[^>]+>", text)

print(match)
