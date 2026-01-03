#二进制文件的读取和写入
#二进制文件包含：图片、电影、音乐、文本等等。

src_file=open('logo.png',rb)            #rb读取二进制文件，src_file源文件
target_file=open('copylogo.png',wb)     #wb写入二进制文件，target_file是目标文件
target_file.write(src_file.read())      #边读边写
target_file.close()                     #完事后关闭
src_file.close()                        #完事后关闭