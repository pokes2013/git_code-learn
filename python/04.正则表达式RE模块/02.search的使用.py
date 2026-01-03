import re

# 02、search，只匹配第一个

# 匹配规则，\d是数字，点是3.11的点
pattern = "\d\.\d+"
# 待匹配的字符
s1 = "I study Python 3.11 every day Python2.7 I love you"
match = re.search(pattern, s1)
print(match)    #只要匹配到第一个然后就结束，结果：<re.Match object; span=(15, 19), match='3.11'>
print(match.group())


