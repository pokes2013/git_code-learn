:softshare
IF "%~1"=="" GOTO :EOF
set time1=%time:~0,2%%time:~3,2%%time:~6,2%
ffmpeg -i "%~1" -vcodec h264 -b:v 0 -preset veryfast -vf scale=960:-2 "%~dpn1_ok.mp4"
set time2=%time:~0,2%%time:~3,2%%time:~6,2%
set /a time3=%time2%-%time1%
set /a time4=(%time2%-%time1%)/60
echo haoshi:%time3%miao>>%USERPROFILE%\Desktop\logs.txt
echo haoshi:%time4%fenzhong>>%USERPROFILE%\Desktop\logs.txt
echo %~1-%date:~0,4%%date:~5,2%%date:~8,2%-%time:~0,2%%time:~3,2%>>%USERPROFILE%\Desktop\logs.txt
SHIFT & GOTO:softshare