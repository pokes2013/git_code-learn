# 文件的追加及写入操作

# 当文件不存在W会创建
# 了解flush和close的特点

## w模式

import time

#
f = open("D:/code/python/04.文件操作/ceshi.txt", "w", encoding="UTF-8")
f.write("hello word")  # 虽然写入成功，但是文件中没有内容，是因为文件内容在内存中。
f.flush()  # 将内存中积攒的程序，刷新写入到硬盘中
time.sleep(60)  # 程序停止6W秒，才能看见f.flush的效果
f.close()  # 其实在这里我们的close方法内置了flush的方法，既然内置上面的就显得多余了

# 小结
# w属性是写入，当ceshi.txt文件中有之前的内容，则会先清空原内容，再写入当前内容。如果要想追加则用a。

## a模式

# 原油内容：hello word

f = open("D:/code/python/04.文件操作/ceshi.txt", "a", encoding="UTF-8")
f.write("hello word2")
f.close()

# a属性追加的内容不会换行
# 运行结果：hello wordhello word2
# 如果想换行，我们可以加\n

f = open("D:/code/python/04.文件操作/ceshi.txt", "a", encoding="UTF-8")
f.write("\nhello word3")
f.close()
