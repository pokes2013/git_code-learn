@echo off
(for /f %%i in ('type "C:\Temp\wenjian01.txt"') do (
    echo,sy+%%i
))>"C:\Temp\wenjian02.txt"