package main

import "fmt"

func main() {
	a := 10
	str := "tom"
	f1 := func() {
		fmt.Println(a, str)
	}
	f1()

	//匿名函数
	func() {
		fmt.Printf("a = %d ,str =%s \n", a, str)
	}() // () 实例化

	//带参数匿名函数

	f2 := func(a, b int) {
		fmt.Println(a, b)
	}
	f2(1, 2)

	func(a, b int) {
		fmt.Println(a, b)
	}(1, 2)
	// 带返回值得匿名函数
	ret := func(a, b int) (result int) {
		fmt.Println(a, b)
		//result =a + b
		//return
		return a + b
	}(1, 2)

	fmt.Print(ret)

}
