import re

# 1、match，匹配开头

# 匹配规则，\d是数字，点是3.11的点
pattern = "\d\.\d+"
# 待匹配的字符
s1 = "I study Python 3.11 every day"
# 匹配， re.I是忽略大小写
math = re.match(pattern, s1, re.I)
print(math)  # 结果：None，为什么没有找到？因为match是从头开始找

s2 = "3.11Python I study every day"
match2 = re.match(pattern, s2, re.I)
print(match2)  # 结果找到了：<re.Match object; span=(0, 4), match='3.11'>

# <re.Match object; span=(0, 4), match='3.11'>
# span=(0, 4)，是位置字符串的下标
# match='3.11'，匹配到的内容

# 那怎么拿到3.11这个值呢？
print("匹配值的起始位置：", match2.start())  # 匹配值的起始位置： 0
print("匹配值的结束位置：", match2.end())  # 匹配值的结束位置： 4
print("匹配区间的位置元素：", match2.span())  # 匹配区间的位置元素： (0, 4)
print("待匹配的字符串：", match2.string)  # 待匹配的字符串： 3.11Python I study every day
print("匹配的数据:", match2.group())  # 匹配的数据: 3.11
