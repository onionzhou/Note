package main

import "fmt"

func add1(a, b int) int {
	return a + b
}

//**************
type aa int
//给一个类型绑定一个函数
// tmp 就是一个就收者，接收者就是一个传递的参数
func (tmp aa) add2(b aa) aa {
	return tmp + b
}

func main() {
	//面向过程
	r := add1(2, 3)
	fmt.Println(r)
	//面向对象
	var a aa = 2
	r1 := a.add2(3)
	fmt.Println(r1)
	/*
		5
		5
	*/
	//面向对象只是换了一种表现方式
}
