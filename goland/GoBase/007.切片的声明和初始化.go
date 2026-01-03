package main

import "fmt"

func main() {

	//切片的声明，和数组不同的是中括号中没有长度

	var arr1 = []int{1, 2, 3, 4, 5, 6}

	fmt.Println(arr1)      //[1 2 3 4 5 6]
	fmt.Println(len(arr1)) //6

	//切片的遍历
	var arr2 = []string{"php", "java", "golang"}
	for i := 0; i < len(arr2); i++ {
		fmt.Println(arr2[i])
	}

}
