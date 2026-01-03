package main

//单行注释

import "fmt"

func main() {

	//变量
	var name string = "pokes"
	fmt.Println(name)

	//一次声明多个变量
	var b, c int = 1, 2
	fmt.Println(b, c)

	//变量的赋值，自动推导数据类型
	names := "pokes"
	age := 18
	fmt.Println(names, age)

	//查看数据类型
	fmt.Printf("%T,%T", names, age)
}
