import re

# #находит не то, доход в слове подоходный
# text = "подоходный, налог"
# match = re.findall(r"прибыль|обретение|доход", text)
# print(match)

# #так можно сделать, чтобы искал слово отдельно
# text = "подоходный, налог, доход"
# match = re.findall(r"прибыль|обретение|\bдоход\b", text)
# print(match)

# # решение для всех сразу
# text = "подоходный, налог, доход"
# match = re.findall(r"\b(прибыль|обретение|доход)\b", text)
# print(match)

# text = "подоходный, налог, доход"
# match = re.findall(r"\b(прибыль|обретение|доход)\b", text)
# print(match)

"""
^ - начало текста (с флагом re.MULTILINE - начало строки)

$ - конец текста (с флагом re.MULTILINE - позиция перед символом переноса строки \n)

\A - начало текста

\b - граница слова (внутри символьных классов [] соответствует символу BACKSPASE)

\B - граница не слова (зависит от флага re.ASCII)

\Z - конец текста

(?=exp) - проверка на совпадение с выражением exp продолжения строки.
При этом позиция поиска не смещается на выражение exp (опережающая проверка).

(?!exp) - проверка на несовпадение с выражением exp продолжения строки.
(Также опережающая проверка)

(?<=exp) - проверка на совпадение с выражением exp хвоста уже обработанной (проверенной)
строки. Она также называется позитивной ретроспективной проверкой.

(?<!exp) - проверка на несовпадение с выражением exp хвоста уже обработанной (проверенной) строки. 
Она называется негативной ретроспективной проверкой"""

text = """
<!DOCTYPE html>
<html>
<head>
    <meta http-equiv="Content-Type" content="text/html" charset="UTF-8">
    <meta name="viewport" content="width-device-width, initial-scale=1.0">
    <title>Уроки по Python</title>
</head>
<body>
<script type="text/javascript">
let o = document.getElementById('id_div');
console.log(obj);
<p align=center>Hello word!</p>
</script>
</body>
</html>"""

# match = re.findall(r"^<script.*?>([\w\W]+)(?=</script>)", text, re.MULTILINE)
# print(match)

# # появилось выражение </script>
# match = re.findall(r"^<script.*?>([\w\W]+)(?<=</script>)", text, re.MULTILINE)
# print(match)

# точка не включает символ переноса строки, а он в данной выражении есть, поэтому ставим [\w\W]
# match = re.findall(r"^<script.*?>(.+)(?<=</script>)", text, re.MULTILINE)
# print(match)

# match = re.findall(r"([-\w]+)[ \t]*=[ \t]*[\"']([^\"']+)(?<![ \t])", text, re.MULTILINE)
# print(match)

# match = re.findall(r"([-\w]+)[ \t]*=[ \t]*(?P<q>[\"'])?(?(q)([^\"']+(?<![ \t]))|([^ \t>]+))", text)
# print(match)


# re.A или re.ASCII - При этом флаге проверки \b, \B, \s, \S, \w, \W действуют так, как если бы они применялись
# к тексту, содержащему только символы ASCII (по умолчанию используется Юникод re.U / re.UNICODE и лучше оставаться в этом режиме)
#
# re.I или re.IGNORECASE - Проверка без учета регистра символов
#
# re.M или re.MULTILINE - Влияет на проверки ^ и $. Начало ^ считается началом строки (сразу после
# символа \n или начало текста). Конец $ считается в позиции перед \n (или конец строки)
#
# re.S или re.DOTALL - При установке этого флага сивол . также включает символ переноса строки \n.
#
# re.X или re.VERBOSE - Позволяет включать в регулярные выражения пробелы и комментарии
#
# re.DEBUG - Включает режим отладки при компиляции регулярного выражения

# match = re.findall(r"""([-\w]+)            #выделяем атрибут
#                     [ \t]*=[ \t]*          #далее, должно идти равно
#                     (?P<q>[\"'])?          #проверяем наличие кавычки
#                     (?(q)([^\"']+(?<![ \t]))|([^ \t>]+))     #выделяем значение атрибута
#                     """,
#                     text, re.MULTILINE|re.VERBOSE)
# print(match)


# (?flags), где flags - один или несколько флагов:
# a - то же самое, что и re.ASCII;
# i - соответствует re.IGNORECASE
# m - re.MULTILINE
# s - re.DOTALL
# x - re.VERBOSE

text = "Python, python, PYTHON"
match = re.findall(r"(?im)python", text)

print(match)