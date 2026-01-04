package main

import "fmt"

func main() {
	var score int = 45

	// if score > 90 && score <= 100 {
	// 	fmt.Println("A")
	// }
	// if score > 80 && score <= 90 {
	// 	fmt.Println("B")
	// }
	// if score > 70 && score <= 80 {
	// 	fmt.Println("C")
	// }
	// if score > 60 && score <= 70 {
	// 	fmt.Println("D")
	// }

	if score > 90 && score <= 100 {
		fmt.Println("A")
	} else if score > 80 && score <= 90 {
		fmt.Println("B")
	} else if score > 70 && score <= 80 {
		fmt.Println("C")
	} else if score > 60 && score <= 70 {
		fmt.Println("D")
	} else {
		fmt.Println("不及格")
	}

}
