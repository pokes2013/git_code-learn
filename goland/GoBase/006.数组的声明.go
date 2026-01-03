package main

import (
	"fmt"
)

//数组的声明

func main() {

	//方法1：
	var arr1 [3]int //声明

	//初始化
	arr1[0] = 10
	arr1[1] = 20
	arr1[2] = 30
	fmt.Println(arr1)

	//方法2：声明的同时初始化
	var arr2 = [3]string{"php", "java", "golang"}
	fmt.Println(arr2)

	//方法3：数组长度不确定（常用）
	//var arr3 = [...]string{"php", "java", "golang", "c++"}
	var arr3 = [...]string{}
	fmt.Println(arr3)

	//方法3：指定索引
	var arr4 = [...]int{1: 2, 2: 3}
	fmt.Println(arr4)

	//数组的遍历
	//方法1：
	for i := 0; i < len(arr2); i++ {
		fmt.Println(arr2[i])
	}

	//方法2：
	for k, v := range arr2 {
		fmt.Println(k, v)
	}

	//方法3：
	var videoExtensions = []string{".mp4", ".mov", ".avi", ".mkv"}

	for _, item := range videoExtensions {
		fmt.Println(item)
	}

	//下划线表示：忽略索引
	//ext表示数组中的元素
}
