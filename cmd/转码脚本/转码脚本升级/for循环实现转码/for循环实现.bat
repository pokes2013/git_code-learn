@echo off
for -f %%i in (data.txt) do (
	ffmpeg -i %%i -c:v libx264 -x264-params crf=22:vbv-maxrate=3000:vbv-bufsize=6000 -s 1280x720 "%~dp1\%~nx1_ok.mp4"
	echo %%i >> %~dp1\%~nx1_ok.txt

)

echo 视频-[%~dp1\%~nx1_ok.mp4]转码成功
pause