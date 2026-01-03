package main

import "fmt"

type Student struct {
	Age int
}

type Person struct {
	Age int
}

func main() {
	var s Student=Student{10}
	var t Person=Person{30}

	//结构体的转换，将Person的t转为Student
	s=Student(t)
	fmt.Println(s)
	fmt.Println(t)
}