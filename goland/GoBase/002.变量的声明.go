package main

//单行注释

import "fmt"

func main() {

	//变量的声明
	var a, b, c int

	//变量初始化
	a = 10
	b = 20
	c = a + b
	fmt.Println(c) //30

	//声明的同时初始化变量
	var name string = "pokes"
	fmt.Println(name) //pokes

	//一次声明多个变量
	var d, e int = 1, 2
	fmt.Println(d, e) //1 2

	//变量的赋值，自动推导数据类型
	names := "pokes"
	age := 18
	fmt.Println(names, age) //pokes 18

	//查看数据类型
	fmt.Printf("%T,%T", names, age) //string,int
}
