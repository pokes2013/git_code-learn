@echo off

::提取视频文件名
DIR *.avi *.rmvb *.rm *.asf *.divx *.mpg *.mpeg *.mpe *.wmv *.mp4 *.mkv *.vob  /B>C:\Temp\wenjian01.txt

::给提取的视频文件名加pokes防止替换
(for /f %%i in ('type "C:\Temp\wenjian01.txt"') do (echo,pokes+%%i.mp4))>"C:\Temp\wenjian02.txt"

::生成索引文件
for /f %%i in (C:\Temp\wenjian02.txt) do type nul>%%i
move pokes* C:\Temp\