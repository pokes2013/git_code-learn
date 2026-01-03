lst=[40,41,42,43,44]
lst=lst[1:]           #从标号（索引）的位置开始，一直切到最后一个元素




lst2=lst[1:3]         #左闭右开，包含索引为1的元素，但是不包含索引为3的元素
print(lst2)
lst3=lst[:]
print(lst3)
print(lst[-4:])