package main

import "fmt"

func main() {
	//求1+2+3+4....100的和
	sum := 0
	for i := 0; i <= 100; i++ {
		sum += i

	}
	fmt.Println(sum) //5050
}
