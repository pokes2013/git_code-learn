:softshare
IF "%~1"=="" GOTO :EOF
ffmpeg -i "%~1" -c:v libx264 -x264-params crf=22:vbv-maxrate=3000:vbv-bufsize=6000 -s 1280x720 "%~dpn1_ok.mp4"
echo %~1-%date:~0,4%%date:~5,2%%date:~8,2%-%time:~0,2%%time:~3,2%>>%~dp0\log\%~x1.txt
SHIFT & GOTO:softshare