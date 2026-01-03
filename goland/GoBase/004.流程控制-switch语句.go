package main

import "fmt"

func main() {
	var score int
	fmt.Println("1、上海；2、北京；3、西安；4、新疆")
	fmt.Println("请选择目的地（请输入编号）：")

	//接受键盘输入并赋值给score变量
	fmt.Scanln(&score)

	switch score {
	case 1:
		fmt.Println("开往上海")
	case 2:
		fmt.Println("开往北京")
	case 3:
		fmt.Println("开往西安")
	case 4:
		fmt.Println("开往新疆")

	}
}
