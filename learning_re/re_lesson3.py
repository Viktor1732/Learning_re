import re

# text = "lat = 5, lon=7, a= 9"
# match = re.findall(r"\w\s*=\s*\d+", text)

# match = re.findall(r"lat\s*=\s*\d+|lon\s*=\s*\d+", text)

# match = re.findall(r"(lat|lon)\s*=\s*\d+", text)

# match = re.findall(r"((lat|lon)\s*=\s*\d+)", text)

# match = re.findall(r"(lat|lon)\s*=\s*(\d+)", text)

# match = re.findall(r"(?:lat|lon)\s*=\s*\d+", text)


text = "<p>Картинка <img src='bg.jpg'> в тексте</p>"
match = re.findall(r"<img\s+[^>]*src=[\"'](.+?)[\"']", text)
print(match)
