@echo off

DIR *.avi *.rmvb *.rm *.asf *.divx *.mpg *.mpeg *.mpe *.wmv *.mp4 *.mkv *.vob *.flv /B>C:\Temp\wenjian.txt

echo 提取文件名OK！

for %%i in ("%cd%") do echo %%~ni>C:\Temp\muluming.txt

echo 提取目录名OK！

for /f %%i in (C:\Temp\muluming.txt) do ( set commitid=%%i)

md D:\00suoying2022\归档-%commitid%

copy *.txt D:\00suoying2022\归档-%commitid%

echo 创建"D:\00suoying2022\归档-%commitid%"目录OK!

for /f %%i in (C:\Temp\wenjian.txt) do echo nul>D:\00suoying2022\%%i.mp4

echo 生成索引文件OK!

move D:\00suoying2022\*.mp4 D:\00suoying2022\归档-%commitid%

echo 复制到归档目录OK!

echo 成功,请按任意键退出！

pause