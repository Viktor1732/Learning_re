import re

# text = "lat = 5, lon=7, a= 9"
# match = re.findall(r"\w\s*=\s*\d+", text)

# match = re.findall(r"lat\s*=\s*\d+|lon\s*=\s*\d+", text)

# match = re.findall(r"(lat|lon)\s*=\s*\d+", text)

# match = re.findall(r"((lat|lon)\s*=\s*\d+)", text)

# match = re.findall(r"(lat|lon)\s*=\s*(\d+)", text)

# match = re.findall(r"(?:lat|lon)\s*=\s*\d+", text)


# text = "<p>Картинка <img src='bg.jpg'> в тексте</p>"
#
# match = re.findall(r"<img\s+[^>]*src=[\"'](.+?)[\"']", text)
#
# match = re.findall(r"(<img)\s+[^>]*src*=(?P<qqq>[\"'])(.+?)(?P=qqq)", text)
# print(match)

# with open("p_course.xml", 'r') as f:
#     lon = []
#     lat = []
#     for text in f:
#         match = re.findall(r"<point\s*[^>]*lon=([\"\'])(\d.*)\1\s*lat=\1(\d.*)\1", text)
#         if len(match) > 0:
#             lon.append(match[0][1])
#             lat.append(match[0][2])
#     print(lon, lat, sep="\n")

with open("p_course.xml", 'r') as f:
    lon = []
    lat = []
    for text in f:
        match = re.search(r"<point\s*[^>]*lon=([\"\'])(?P<lon>\d.*)\1\s*lat=\1(?P<lat>\d.*)\1", text)
        if match:
            v = match.groupdict()
            if "lon" in v and "lat" in v:
                lon.append(v["lon"])
                lat.append(v["lat"])
    print(lon, lat, sep="\n")

