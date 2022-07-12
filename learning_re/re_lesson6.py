import re

# re.match(pattern, string, flags)
# pattern - регулярное выражение
# string - анализируемая строка
# flags - один или несколько флагов

# text = "+7(908)324-54-22"
# m = re.match(r"\+7\(\d{3}\)\d{3}-\d{2}-\d{2}", text)
# print(m)


# re.split(pattern, string, flags) - разбивка строки по заданному шаблону

# text = """<point lon="40.8483" lat="53.6533" />
# <point lon="40.8477" lat="53.2445" />; <point lon="40.8965" lat="53.4345" />
# <point lon="40.8965" lat="53.2235" />; <point lon="40.9544" lat="53.9056" />
# """
# ar = re.split(r"[\n;,]+", text)
# print(ar)


# re.sub(pattern, repl, string, count, flags) - замена в строке найденных совпадений
text = """Москва
Казань
Сочи
Самара
Красноярск
Уфа"""

# list_town = re.sub(r"\s*(\w+)\s*", r"<option>\1</option\n", text)
# print(list_town)

count = 0
def replFind(m):  # Match
    global count
    count += 1
    return f"<option value='{count}'>{m.group(1)}</option>\n"
#
# # list_town = re.sub(r"\s*(\w+)\s*", replFind, text)
# print(list_town)


# re.subn(pattern, repl, string, count, flags) -метод возращает не только строку, но и число произведенных замен
# list_town, total = re.subn(r"\s*(\w+)\s*", r"<option>\1<option>\n", text)
# print(list_town, total)


#re.compile(pattern, flag) - производит компиляцию рег.выражения и возвращает экземпляр класса Pattern
rx = re.compile(r"\s*(\w+)\s*")
list_town, total = rx.subn(r"<option>\1</option>\n", text)
list_town2 = rx.sub(replFind, text)
print(list_town, total, list_town2, sep="\n")
