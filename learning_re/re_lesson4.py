import re


text = "<p>Картинка <img alt='картинка' src='bg.jpg'> в тексте</p>"
match = re.findall("<img\s+[^>]*src\s*=\s*[^>]+>", text)





print(match)