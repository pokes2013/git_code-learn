package main

import (
	"fmt"
	"os"
	"os/exec"
	"path/filepath"
	"strings"
	"time"
)

// 函数：检验是否是视频文件，下面遍历会调用
func isVideoFile(path string) bool {
	//定义视频文件的后缀
	var videoExtensions = []string{".mp4", ".mov", ".avi", ".mkv"}

	for _, ext := range videoExtensions {
		if strings.HasSuffix(strings.ToLower(path), ext) {
			return true
		}
	}
	return false
}

// 遍历视频文件

//	遍历所有文件：并判断是否是视频文件
//	判断的依据是isVideoFile函数
//	返回一个数组
//	数组中是绝对路径

func listVideoFiles(dirPath string) []string {

	//获取所有文件，并检验错误
	files, err := os.ReadDir(dirPath)
	if err != nil {
	}
	//定义一个空的数组用于存放视频文件
	var videoFiles []string
	//遍历文件
	for _, file := range files {
		if file.IsDir() {
			continue
		}
		//拼接绝对路径
		path := filepath.Join(dirPath, file.Name())

		//如果是视频文件则写入到videoFiles数组中
		if isVideoFile(path) {
			videoFiles = append(videoFiles, path)
		}
	}
	return videoFiles
}

// 函数，从绝对路径中获取文件名、扩展名
func getInName(absolutePath string) string {
	//请传入一个绝对路径的文件："/path/to/your/file.txt"

	// 使用filepath.Base获取文件名和扩展名
	fileNameWithExtension := filepath.Base(absolutePath)
	//fileName := fileNameWithExtension[:len(fileNameWithExtension)-len(filepath.Ext(absolutePath))]
	//fileExtension := filepath.Ext(absolutePath)
	//outvideo := fileName + "_ok" + fileExtension
	return fileNameWithExtension
}

func getOutName(InName string) string {
	fileNameWithExtension := filepath.Base(InName)
	fileName := fileNameWithExtension[:len(fileNameWithExtension)-len(filepath.Ext(InName))]
	fileExtension := filepath.Ext(InName)
	outvideo := fileName + "_ok" + fileExtension
	return outvideo

}

// 函数转码拼接cmd
func ffmpegcmd(invideo, outvideo string) {
	cmd := exec.Command(
		"ffmpeg",
		"-i",
		invideo,
		"-vcodec h264",
		"-preset veryfast",
		"-crf 19.1",
		"-maxrate 2000k",
		"-bufsize 3000k",
		"-r 29.9",
		"-vf scale=1280:-2",
		outvideo,
	)
	fmt.Println(cmd)
	err := cmd.Run() // 获取标准输出和标准错误
	if err != nil {
		fmt.Println("转码失败")
	}
}

// 休息时间
func sleeptime(miao int) {
	slpTime := miao * 1000
	time.Sleep(time.Duration(slpTime) * time.Millisecond)
}

func main() {
	videolist := listVideoFiles("E:\\temptest")
	for _, videopath := range videolist {

		invideo := getInName(videopath)
		fmt.Println(invideo)
		outvide := getOutName(invideo)
		fmt.Println(outvide)
		//ffmpegcmd(invideo, outvide)
		//
		////休息1分钟
		//sleeptime(3)
	}

}
