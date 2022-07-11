import re

# text = "<font color=#CC0000>"
# match = re.search(r"(\w+)=(#[\d\w\W]{6})\b", text)

# print(match.group())
# print(match.group(1))
# print(match.group(2))
# print(match.group(0, 1, 2))

# Содержит индекс последней сохраняющей группы
# print(match.lastindex)

# Позиция начала в тексте определенной группы
# print(match.start(1))

# Позиция окончания в тексте определенной группы
# print(match.end(1))

# Позиция начала и окончания определенной группы
# print(match.span(1))

# Первый и последний индекс в пределах которых осуществлялась проверка в тексте
# начальный идекс
# print(match.pos)
# конечный индекс
# print(match.endpos)

# Получаем скомпилированный шаблон
# print(match.re)

# Возвращаем анализируемую строку
# print(match.string)

# Получили имя группы и значение
# text = "<font color=#CC0000>"
# match = re.search(r"(?P<key>\w+)=(?P<value>#[\d\w\W]{6})", text)

# print(match.groupdict())

# возвращает имя последней группы или None, если группы нет
# print(match.lastgroup)

# Формируем строку с использованием сохраненных групп
# Обычно используются имена
# print(match.expand(r"\g<key>:\g<value>"))
# print(match.expand(r"\1:\2"))

# \g<name> - обращение к группе по имени
# \1, \2, ... - обращение к группе по номеру


# Метод re.search
# re.search(pattern, string, flags)
# pattern - регулярное выражение
# string - анализируемая строка
# flags - один или несколько флагов

# Метод re.search выделяет только первый атрибут, второй игнорируется
# text = "<font color=#CC0000 bg=#ffffff>"
# match = re.search(r"(?P<key>\w+)=(?P<value>#[\da-fA-F]{6})\b", text)
# print(match)


# Метод re.finditer(pattern, string, flags) - возвращает итерируемый объект
# text = "<font color=#CC0000 bg=#ffffff>"
# for match in re.finditer(r"(?P<key>\w+)=(?P<value>#[\da-fA-F]{6})\b", text):
#     print(match)


# Метод re.findall(pattern, string, flags) - получаем список найденных вхождений
text = "<font color=#CC0000 bg=#ffffff>"
match = re.findall(r"(?P<key>\w+)=(?P<value>#[\da-fA-F]{6})\b", text)
print(match)