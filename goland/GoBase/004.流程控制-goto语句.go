package main

import "fmt"

func main() {
	fmt.Println("hell golang1")
	fmt.Println("hell golang2")
	goto pokes
	fmt.Println("hell golang3")
	fmt.Println("hell golang4")
	fmt.Println("hell golang5")
	pokes:
	fmt.Println("hell golang6")
	fmt.Println("hell golang7")
	fmt.Println("hell golang8")
	fmt.Println("hell golang9")
}

//运行结果：
//hell golang1
//hell golang2    //345被跳过了
//hell golang6
//hell golang7
//hell golang8
//hell golang9
