package main

import "fmt"

//闭包

//getsum函数返回值为一个函数，而且返回的是一个匿名函数，匿名函数返回的sum

func getsum() func(int) int {
	var sum int = 10
	return func(num int) int {
		sum = sum + num
		return sum
	}
}

//返回的匿名函数+匿名函数以外的变量num

func main() {
	f := getsum()
	fmt.Println(f(1)) //11
	fmt.Println(f(2)) //13

	//上行的结果我们的预期是12，结果是13，为什么？
	//因为他是在fmt.Println(f(1))的基础上加的，也就是11+2

	fmt.Println(f(3)) //16
}
