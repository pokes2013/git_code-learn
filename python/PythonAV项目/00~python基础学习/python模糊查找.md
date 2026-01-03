# python模糊查找



## 参考文献：

https://blog.csdn.net/qq_41192383/article/details/86587829

参考代码：

```python
import os
path = r'F:\temp\test'
files = os.listdir(path)
for f in files:
    if f.endswith('.png') and 'fish' in f:
        print('Look! I found this \n'+f)
```

## 思路



读取文件

获取文件名1：abc

获取文件名2：123

查找是否同时包含 abc和123

到数据库中查找

如果有打印到文件中

如果没有跳过



