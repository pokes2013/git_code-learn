
REM 去除文件_ok中OK前面的.mp2


@echo off
Setlocal Enabledelayedexpansion
	set "str=_ok"
	for /f "delims=" %%i in ('dir /b *.mp4') do (
	set "var=%%i" & ren "%%i" "!var:%str%=!")