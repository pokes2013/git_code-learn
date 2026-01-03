ffmpeg -i "%~1" -vcodec h264 -preset veryfast -b:v 0 "%~dpn1_ok.mp4"
rem ffmpeg -i "%~1" -vcodec h264 -preset veryfast -b:v 0 -s 1280x720 "%~dpn1_ok.mp4"