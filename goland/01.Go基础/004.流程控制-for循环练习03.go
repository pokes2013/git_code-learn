package main

import "fmt"

func main() {
	//练习：打印1-100之间所有是9的倍数的整数的和，以及个数？
	sum := 0
	count := 0
	for i := 1; i <= 100; i++ {
		if i%9 == 0 {
			sum += i
			count++
		}
	}
	fmt.Println(sum,count)
}
