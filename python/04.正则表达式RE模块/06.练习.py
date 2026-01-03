import re

# 欧美
# pattern = "([A-Za-z]{3,10}\.){3,20}"
# str = "Jana.Cova.Video.Nasty.XXX.720p.WEBRip.MP4-OHRLY[rarbg].H264超级无损[欧美]"
# list = re.findall(pattern, str)
# print(list)


pattern = "![A-Za-z]{3,5}-\d{3,10}"
str = "abc-123.mp4"
list = re.findall(pattern, str)
print(list)


