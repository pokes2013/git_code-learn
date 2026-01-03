@echo off

echo 注意:自动裁剪现阶段只支持裁剪片头，暂不支持片尾！
echo 时间戳定位并不精确，最多只能算是粗剪，请酌情使用！
echo 造成数据丢失概不负责！
echo.
echo 无法使用可能出现的问题？
echo 1.没有安装ffmpeg;
echo 2.没有添加到环境变量.
echo.

echo 作者：亦良cool  邮箱：pokes@163.com
echo -------------------------------------------------
echo 请依次输入分钟和秒数，必须是两位整数！
echo 例如：0分30秒，分钟：00，秒数：30
echo -------------------------------------------------

set /p shi=请输入小时：

set /p fen=请输入分钟:

set /p miao=请输入秒数:



ffmpeg -i "%~1" -ss 00:00:00 -to %shi%:%fen%:%miao% -c copy -avoid_negative_ts 1 "%~dpn1_ok.mp4"
