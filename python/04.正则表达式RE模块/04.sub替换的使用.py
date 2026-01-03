import re

# 02、sub，替换

# 替换的词
pattern = "黑客|破解|反爬"
# 待匹配的字符
s1 = "我想学习Python，想破解一些VIP视频，Python可以实现反爬吗？"

match = re.sub(pattern, "***", s1)
print(match)  # 我想学习Python，想***一些VIP视频，Python可以实现***吗？

