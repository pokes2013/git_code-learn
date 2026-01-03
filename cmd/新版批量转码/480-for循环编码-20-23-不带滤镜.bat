REM 问题：生成的文件出现类似这样的状况abc-123.mp4_ok.mp4


@echo off 
Setlocal Enabledelayedexpansion


set yuan_folder=待删除


REM 将源文件统一放到input里面方便删除，这里不建议自动删除，请自行手动删除

IF EXIST %yuan_folder% (
		echo %yuan_folder%目录存在，正在去除文件名中的空格
	) ELSE (
		md %yuan_folder%
		echo %yuan_folder%创建成功，正在去除文件名中的空格
	)





REM 去除文件中的空格


set "str= "
for /f "delims=" %%i in ('dir /b *.ts,*.avi,*.mp4,*.wmv,*.flv,*.mkv,*.rmvb,*.rm,*.mov') do (set "var=%%i" & ren "%%i" "!var:%str%=!")


REM 转码信息

REM 过滤出所有视频文件

set vido='*.ts,*.avi,*.mp4,*.wmv,*.flv,*.mkv,*.rmvb,*.rm,*.mov'

for %%a in (%vido%) do (

REM 转码

  	ffmpeg -i "%%a" -vcodec h264 -preset veryfast -tune:v ssim -qmin 20 -crf 23 -maxrate 1000k -bufsize 500k -r 29.97 -vf scale=720:-2 "%%a_ok.mp4"


echo ---------------------------------------->>logs.txt

REM 视频时长
	ffprobe "%%a" -select_streams v -show_entries stream=duration -of default=nk=1:nw=1 -v quiet >> logs.txt

	echo "%%a"转换完成>>logs.txt
	move "%%a" %yuan_folder%\
	
)

REM 重命名类似这样的状况abc-123.mp4_ok.mp4

set "str=.mp4"
for /f "delims=" %%i in ('dir /b *.mp4') do (
set "var=%%i" & ren "%%i" "!var:%str%=!".mp4)



pause
