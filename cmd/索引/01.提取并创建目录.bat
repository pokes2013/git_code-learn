@echo off

::提取目录
dir /b > C:\Temp\muluming.txt

::创建目录
for /f %%i in (C:\Temp\muluming.txt) do md %%i
pause