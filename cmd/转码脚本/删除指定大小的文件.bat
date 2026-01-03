
taskkill /f /t /im NegativeEncoder.exe
taskkill /f /t /im NVEncC64.exe
for /r %%F in (*.png *.mp4) do if %%~zF LSS 100000000 del "%%F"



REM （1）1000的单位是Byte
REM （2）（*）可以指定具体删除的文件扩展名如：(*.png *.gif)，用空格分隔。
REM （3）equ 等于，LSS小于