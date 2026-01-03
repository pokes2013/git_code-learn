package main

import (
	"bufio"
	"fmt"
	"os"
	"os/exec"
	"path/filepath"
	"strings"
)

//ffmpeg -i "%~1"       -vcodec h264 -preset veryfast -crf 19.1 -maxrate 2000k -bufsize 3000k -r 29.9 -vf scale=1280:-2 "%~dpn1_ok.mp4" && echo 转换OK
//ffmpeg -i abc-123.mp4 -vcodec h264 -preset veryfast -crf 19.1 -maxrate 2000k -bufsize 3000k -r 29.9 -vf scale=1280:-2 abc-123_ok.mp4

// TranscodeVideo 使用FFmpeg转码单个视频文件
func TranscodeVideo(inputFilePath, outputFilePath, format string) error {
	// 设置FFmpeg转码参数
	args := []string{
		"-i", inputFilePath,
		"-c:v", "libx264",
		"-c:a", "aac",
		"-s", "1280x720",
		"-preset", "fast",
		"-crf", "23",
		fmt.Sprintf("-f", format),
		outputFilePath,
	}

	// 创建FFmpeg命令对象
	cmd := exec.Command("ffmpeg", args...)

	// 设置命令对象的StdoutPipe和StderrPipe属性，以便监听转码进度
	stdout, err := cmd.StdoutPipe()
	if err != nil {
		return err
	}
	stderr, err := cmd.StderrPipe()
	if err != nil {
		return err
	}

	// 启动FFmpeg进程
	if err := cmd.Start(); err != nil {
		return err
	}

	// 读取并处理标准输出和标准错误
	go func() {
		scanner := bufio.NewScanner(stdout)
		for scanner.Scan() {
			fmt.Println(scanner.Text())
		}
	}()
	go func() {
		scanner := bufio.NewScanner(stderr)
		for scanner.Scan() {
			fmt.Println(scanner.Text())
		}
	}()

	// 等待FFmpeg进程完成
	if err := cmd.Wait(); err != nil {
		return err
	}

	return nil
}

// BatchTranscodeVideos 批量转码视频文件
func BatchTranscodeVideos(inputDir, outputDir, format string) error {
	// 遍历输入目录中的所有视频文件
	files, err := os.ReadDir(inputDir)
	if err != nil {
		return err
	}

	for _, file := range files {
		if !strings.HasSuffix(file.Name(), ".mp4") { // 假设只处理MP4文件，您可以根据需要修改此条件
			continue
		}

		inputFilePath := filepath.Join(inputDir, file.Name())
		outputFilePath := filepath.Join(outputDir, strings.TrimSuffix(file.Name(), ".mp4")+"."+format)

		// 转码单个视频文件
		if err := TranscodeVideo(inputFilePath, outputFilePath, format); err != nil {
			return err
		}
	}

	return nil
}

func main() {
	inputDir := "."      // 输入目录路径
	outputDir := "./out" // 输出目录路径
	format := "mp4"      // 目标格式

	// 批量转码视频文件
	if err := BatchTranscodeVideos(inputDir, outputDir, format); err != nil {
		fmt.Printf("Batch transcode failed: %v\n", err)
		return
	}

	fmt.Println("Batch transcode completed successfully!")
}

//
//
//func ffmpegcmd(inputFilePath, outputFilePath string) {
//
//	args := []string(
//		"-i",
//		inputFilePath,
//		"-vcodec h264",
//		"-preset veryfast",
//		"-crf 19.1",
//		"-maxrate 2000k",
//		"-bufsize 3000k",
//		"-r 29.9",
//		"-vf scale=1280:-2",
//		outputFilePath,
//		fmt.Sprintf("-f", format), outputFilePath)
//	cmd:=exec.Command("ffmpeg",args...)
//
//func main() {
//
//	//cmd := exec.Command("dir", "Hello, World!")
//	//output, err := cmd.CombinedOutput() // 获取标准输出和标准错误
//	//if err != nil {
//	//	panic(err)
//	//}
//	//fmt.Println(string(output))
//
//	ffmpegcmd("001.mp4", "001_ok.mp4")
//
//}
