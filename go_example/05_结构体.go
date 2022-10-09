package main

import "fmt"

type Student struct {
	id   int
	name string
	sex  byte // 字符
	age  int
	addr string
}

func main() {

	//顺序初始化，必须初始化
	var s1 Student = Student{0, "tom", 'm', 18, "sc"}
	fmt.Println("s1 = ", s1)
	// 指定成员初始化，没有初始化的成员，自动赋值为0
	var s2 Student = Student{addr: "sc"}
	fmt.Println("s2 = ", s2)
	/*
		s1 =  {0 tom 109 18 sc}
		s2 =  {0 0 0 sc}
	*/
}
