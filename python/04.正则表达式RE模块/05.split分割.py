import re

# 05、split，分割


# 待匹配的字符
s1 = "https://www.bilibili.com/video/BV16hUaYQEsn/?spm_id_from=333.1007.tianma.1-1-1.click"

# 匹配的字符
pattern = "[?|=]"  # 以问号或者等号分割

# 返回一个list
s1List = re.split(pattern, s1)
print(s1List)  # ['https://www.bilibili.com/video/BV16hUaYQEsn/', 'spm_id_from', '333.1007.tianma.1-1-1.click']

# 遍历拿到每个值
for item in s1List:
    print(item)
