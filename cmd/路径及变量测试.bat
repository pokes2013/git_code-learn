@echo off

set /p pokes=请拖拽文件夹到此窗口,按回车键继续：

::获取脚本文件的绝对路径带引号，含文件名
echo %0

::获取文件绝对路径含文件名
echo %1


::获取脚本程序路径不含文件名
echo %~dp0


::xuexi

@echo off
echo 当前盘符：%~d0
echo 当前路径：%~p0
echo 当前盘符和路径：%~dp0
echo 当前批处理(%0文件)全路径：%~f0
echo 当前盘符和路径的短文件名格式：%~sdp0
echo 当前CMD默认目录：%cd%



echo %~x1


pause