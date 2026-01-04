package main

import "fmt"

// map，俗称映射

func main() {

	// 方法1：
	// map的声明，如果只声明不赋值，则不会分配内存空间
	var a map[int]string
	//赋值，中括号内为学号，学号对应了姓名
	a = make(map[int]string, 10)
	a[20095452] = "张三"
	a[20095451] = "李思"
	a[20095453] = "小明"
	fmt.Println(a) //map[20095451:李思 20095452:张三 20095453:小明]

	// 方法2：
	b := make(map[int]string)
	b[20095452] = "张三"
	b[20095451] = "李思"
	b[20095453] = "小明"
	fmt.Println(b)

	// 方法3：推荐
	c := map[int]string{
		20095452: "张三",
		20095451: "李思",
		20095453: "小明",
	}
	fmt.Println(c)

	//map的遍历
	for key, value := range c {
		fmt.Println(key,value)

	}
}

