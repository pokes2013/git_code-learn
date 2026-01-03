@echo off & setlocal enabledelayedexpansion

set "s1=00:00:45.240"
set "s2=00:01:30.090"

for /f "tokens=1-4delims=:." %%a in ("%s2%") do (
    set /a "t2=(1%%a %% 100 *3600 + 1%%b %% 100 * 60 + 1%%c %% 100) * 1000 + 1%%d %% 1000"
)

md NEW 2>nul
for %%i in (*.avi *.mkv *.mp4 *.flv) do (
    for /f "tokens=2-5delims=:., " %%a in ('ffmpeg -i "%%i" 2^>^&1 ^| find "Duration:"') do (
        set /a "t=(1%%a%%100*3600+1%%b%%100*60+1%%c%%100)*1000+1%%d0%%1000,t-=t2,ms=t%%1000,t/=1000"
        set /a h=t/3600,m=t%%3600/60,s=t%%60,h+=100,m+=100,s+=100,ms+=1000
        set "t=!h:~1!:!m:~1!:!s:~1!.!ms:~1!"
        ffmpeg -i "%%i" -ss !s1! -to !t! -vcodec copy -acodec copy "NEW\%%i" -y
    )
)
pause