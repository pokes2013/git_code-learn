:softshare
IF "%~1"=="" GOTO :EOF
@rem echo %time%
ffmpeg -i "%~1" -vcodec h264 -preset veryfast -b:v 0 "%~dpn1_ok.mp4" > output.txt 2>&1
@rem echo %time%
echo %~1-%date:~0,4%%date:~5,2%%date:~8,2%-%time:~0,2%%time:~3,2%>>log.txt
SHIFT & GOTO:softshare
@pause
