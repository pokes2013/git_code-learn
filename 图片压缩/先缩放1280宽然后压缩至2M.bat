@echo off
chcp 65001 >nul
setlocal enabledelayedexpansion
:: 2MB字节上限
set "MAX_SIZE=2097152"
set "OUT_DIR=outfiles"

:: 创建输出文件夹
if not exist "%OUT_DIR%" mkdir "%OUT_DIR%"

:: 遍历所有图片
for %%i in (*.jpg *.jpeg *.png) do (
    set "input_file=%%i"
    set "output_file=%OUT_DIR%\%%~ni_ok.jpg"
    echo 【处理】原图：!input_file!
    :: 初次尺寸压缩
    ffmpeg -i "!input_file!" -vf scale=1280:-2 -q:v 8 "!output_file!"
    :: 调用子程序压缩至2M以内
    call :CompressToLimit "!output_file!"
    echo 【完成】输出：!output_file!
    echo.
)

echo =====================================
echo 所有图片处理完毕，压缩文件在 outfiles 文件夹
pause
exit /b

:: 子程序：反复降低画质，限制文件体积
:CompressToLimit
set "target_file=%~1"
for %%f in ("%target_file%") do set "file_size=%%~zf"
set "quality=8"

:inner_loop
if %file_size% leq %MAX_SIZE% exit /b
set /a quality+=2
ffmpeg -i "%target_file%" -q:v %quality% "%target_file%"
for %%f in ("%target_file%") do set "file_size=%%~zf"
goto inner_loop