package main

import "fmt"

type Persons struct {
	Nume string
}

//括号内的per Persons表面看似是传参，其实也是将test方法和Persons结构体绑定

func (per Persons) test() {
	fmt.Println(per.Nume)
}
func main() {

	//创建一个Person对象，xiaoming
	var xiaoming Persons
	xiaoming.Nume = "小明"
	xiaoming.test() //小明

}
