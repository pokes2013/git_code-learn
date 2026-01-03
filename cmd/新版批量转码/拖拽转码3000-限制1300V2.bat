:softshare
IF "%~1"=="" GOTO :EOF


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



rem ::开始时间
set time1=%time:~0,2%%time:~3,2%%time:~6,2%

rem ::ffmpeg转码
ffmpeg -i "%~1" -vcodec h264 -preset veryfast -tune:v ssim -qmin 19.1 -crf 22 -maxrate 1350k -bufsize 2000k -r 25 -vf scale=1280:-2 "%~dpn1_ok.mp4" && echo 转换OK

rem ::移动源文件
move "%~1" %yuan_folder%

rem ::移动目标文件
move "%~dpn1_ok.mp4" %output_folder%


rem ::结束时间
set time2=%time:~0,2%%time:~3,2%%time:~6,2%
rem ::计算所需时间
set /a time3=%time2%-%time1%
set /a time4=(%time2%-%time1%)/60


rem ::日志文件


echo time：%time4% minute>>logs.txt
echo %~1-%date:~0,4%%date:~5,2%%date:~8,2%-%time:~0,2%%time:~3,2%>>logs.txt
echo ------------------------------------------------------------>>logs.txt

rem ::程序休息10分钟后继续执行




SHIFT & GOTO:softshare