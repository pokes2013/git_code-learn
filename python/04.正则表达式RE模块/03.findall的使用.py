import re

# 03、findall，查找所有

# 匹配规则，\d是数字，点是3.11的点
pattern = "\d\.\d+"

# 待匹配的字符
s1 = "I study Python 3.11 every day Python2.7 I love you"


list = re.findall(pattern, s1)
print(list)  # 查找所有并返回一个列表，结果：['3.11', '2.7']

for item in list:
    print(item)
