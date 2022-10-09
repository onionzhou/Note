package main

import "fmt"

type Person struct {
	name string
	sex  byte
	age  int
}

func (person Person) PrintInfo() {
	fmt.Println(person)
}

func (p *Person) SetInfo(n string, s byte, a int) {
	p.name = n
	p.sex = s
	p.age = a
}

func main() {

	p := Person{"tom", 'm', 18}
	var p1 = Person{"tom", 'm', 18}
	p.PrintInfo()
	p1.PrintInfo()

	var p2 Person // 结构体变量
	(&p2).SetInfo("hello", 'f', 20)
	p2.PrintInfo()
	/*
		{tom 109 18}
		{tom 109 18}
		{hello 102 20}
	*/

}
