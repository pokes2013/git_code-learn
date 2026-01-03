# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 16:56:30 2023

@author: Anita
"""

import requests

html = requests.get('https://avmoo.online/cn/star/d16528578f53de5a')  # 得到一个Response对象
html_bytes = html.content  # 属性.content用来显示bytes型网页的源代码
html_str = html_bytes.decode()  # 属性.decode()用来把bytes型的数据解码为字符串型的数据，默认编码格式UTF-8
print(html_str)
