@echo off

set /p pokes=请拖拽文件夹到此窗口,按回车键继续：

::自选转码分辨率和模式

echo 无损源分辨率请输入1 
echo 无损720p请输入2
echo 无损1000p请输入2
echo 无损960p请输入3

set /p input=请选择码率模式：
if "%input%"=="1" goto 720p
if "%input%"=="2" goto 1000p
if "%input%"=="3" goto 960p

:720p
call 720p.bat

:1000p
call 1000p.bat

:960p
call 960p.bat

pause