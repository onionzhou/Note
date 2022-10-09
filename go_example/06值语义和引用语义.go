package main

import "fmt"

type Person struct {
	name string
	sex  byte
	age  int
}

//接收者为 普通变量
func (p Person) SetInfoValue(n string, s byte, a int) {
	p.name = n
	p.sex = s
	p.age = a

	fmt.Printf("SetInfoValue  &p=%p\n", &p)
}

func (p *Person) SetInfoPointer(n string, s byte, a int) {
	p.name = n
	p.sex = s
	p.age = a
	fmt.Printf("SetInfoPointer  &p=%p\n", &p)
}

func main() {
	var s1 Person
	fmt.Printf("&s1 =%p\n", &s1)

	s1.SetInfoValue("tom", 'm', 18)
	fmt.Println("s1 = ", s1)

	(&s1).SetInfoPointer("tom", 'm', 18)
	fmt.Println("s1 = ", s1)
}
