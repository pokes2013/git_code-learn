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
:softshare
IF "%~1"=="" GOTO :EOF
ffmpeg -i "%~1" -c:v libx264 -x264-params crf=22:vbv-maxrate=3000:vbv-bufsize=6000 -s 1280x720 "%~dpn1_ok.mp4"
echo %~dpn1_ok.mp4>>%~dpn1_ok.txt
SHIFT & GOTO:softshare

:1000p
call 1000p.bat

:960p
call 960p.bat

pause