package main

import "fmt"

type Person struct {
	name string
	sex  byte
	age  int
}

//接收者为 普通变量
func (p Person) SetInfoValue() {
	fmt.Printf("SetInfoValue \n")
}

func (p *Person) SetInfoPointer() {

	fmt.Printf("SetInfoPointer \n")

}

func main() {

	p := Person{name: "mkie", age: 19}
	fmt.Printf("main  %p,  %v\n", &p, p)

	f := p.SetInfoValue
	f() // 方法值   隐藏了接收者

	// 方法表达式
	f1 := (*Person).SetInfoPointer
	f1(&p) // 显式把接收者传递过去 --   p.SetInfoPointer
	f2 := (Person).SetInfoValue
	f2(p) // 显式把接收者传递过去 --   p.SetInfoValue

	/*
		main  0xc00004c3c0,  {mkie 0 19}
		SetInfoValue
		SetInfoPointer
		SetInfoValue

	*/
}
