package main

import "fmt"

func main() {
	var n1 int = 19
	var n2 float32 = 4.78
	//var n3 bool = false

	//将整形转为字符串
	var s1 string = fmt.Sprintf("%d", n1)
	fmt.Printf("当前s1数据类型为%T,值为%q.\n", s1, s1)

	//将float32转为字符串
	var s2 string = fmt.Sprintf("%f", n2)
	fmt.Printf("当前s2数据类型为%T,值为%q.\n", s2, s2)

	a := 3
	//查看类型
	fmt.Printf("%T", a) //int
	b := float64(a)
	fmt.Printf("%T", b) //float64

	// 将int类型转换为字符串类型
	c := 16
	fmt.Printf("%T", c) //int
	d := fmt.Sprint(c)
	fmt.Printf("%T", d) //string

	// 将字符串类型转换为int类型
	e := "17"
	fmt.Printf("%T", e) //int
	f := int(c)
	fmt.Printf("%T", f) //string
}
