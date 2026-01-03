package main

import "fmt"

func main() {
	var x int
	var y float64

	fmt.Println("请输入两个数：1、整数，2、浮点数：")
	fmt.Scanln(&x, &y)
	fmt.Println("x", x)
	fmt.Println("y", y)

	//在终端输入两个数时，输入在一行以空格隔开，再回车键！
}
