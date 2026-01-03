REM 视频转码批处理，转码完成之后将源文件统一放到“OK”中


@echo off 
Setlocal Enabledelayedexpansion



REM 1、判断所需目录是否存在


rem ::在这里需要两个目录来分别存放源文件和输出文件
rem ::将源文件统一放到“source_data”里面方便删除，这里不建议自动删除，请自行手动删除
rem ::将输出文件放到“OK”文件夹内

set output_folder=OK

IF EXIST %output_folder% (
		echo %output_folder%目录存在，正在去除文件名中的空格
	) ELSE (
		md %output_folder%
		echo %output_folder%创建成功，正在去除文件名中的空格
	)



set yuan_folder=source_data

IF EXIST %yuan_folder% (
		echo %yuan_folder%目录存在，正在去除文件名中的空格
	) ELSE (
		md %yuan_folder%
		echo %yuan_folder%创建成功，正在去除文件名中的空格
	)



REM 2、去除文件中的空格


set "str= "
for /f "delims=" %%i in ('dir /b *.ts,*.avi,*.mp4,*.wmv,*.flv,*.mkv,*.rmvb,*.rm,*.mov') do (set "var=%%i" & ren "%%i" "!var:%str%=!")



REM 3、转码信息



REM 过滤出所有视频文件

set vido='*.ts,*.avi,*.mp4,*.wmv,*.flv,*.mkv,*.rmvb,*.rm,*.mov'

for %%a in (%vido%) do (

REM 转码

  	ffmpeg -i "%%a" -vcodec h264 -preset veryfast -tune:v ssim -qmin 18 -crf 22.0 -maxrate 2500k -bufsize 5000k -r 29.97 -vf unsharp=5:5:0.06:5:5:0.0,scale=1280:-2 "%%a_ok.mp4"


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


rem ::移动转换成功的文件到output_folder目录中

move *.MP4 %output_folder%\



pause
