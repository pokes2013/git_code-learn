

# 字符串处理的常用方法

print("POKES".lower())  #pokes,转换成小写
print("pokes".upper())  #POKES,转换成小写

# 以字母K分割
print("pokes".split("k"))  #['po', 'es']

# 统计字母k出现的次数
print("pokkkkkeskkk".count("k"))  # 8

# 查询字母k是否出现，如果出现结果返回出现的索引，没出现则返回-1
print("pokes".find("k"))  # 2
print("pooes".find("k"))  # -1

# 判断是否以k开头，返回布尔值
print("pokes".startswith("k"))  # False
print("kpokes".startswith("k"))  # True

# 判断是否以k结尾，返回布尔值
print("pokes".endswith("k"))  # False
print("kpokesk".endswith("k"))  # True


print("abc-123.mp4"[0:-4] )  # True
print("abc-123.mp4"[-4:] )  # True