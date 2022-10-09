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
	fmt.Println(p)
}

func (p *Person) SetInfoPointer(n string, s byte, a int) {
	p.name = n
	p.sex = s
	p.age = a
	fmt.Printf("SetInfoPointer  &p=%p\n", &p)
	fmt.Println(p)
}

func main() {
	//调用的时候 不考虑变量是不是指针

	// 结构体变量是一个指针变量，它能够调用那些方法，这些方法就是一个集合 称为方法集
	p := &Person{"mike", 'm', 19}

	p.SetInfoPointer("mm", 'f', 20)    // func (p *Person) SetInfoPointer()
	(*p).SetInfoPointer("mm", 'f', 20) //  把 *p 转换成p 再调用，等价于上面

	//内部会转换，先把指针P  转成*p 再调用
	p.SetInfoValue("mm", 'f', 20)
	(*p).SetInfoValue("mm", 'f', 20)
	/*
		SetInfoPointer  &p=0xc000006028
		&{mm 102 20}
		SetInfoPointer  &p=0xc000006038
		&{mm 102 20}
		SetInfoValue  &p=0xc00004c440
		{mm 102 20}
		SetInfoValue  &p=0xc00004c480
		{mm 102 20}

	*/

	// 普通变量
	p1 := Person{"mike", 'm', 19}
	p1.SetInfoPointer("mm", 'f', 20) // 内部先把p 转换为&p 再调用，(&p).SetInfoPointer
	p1.SetInfoValue("mm", 'f', 20)

	/*
		SetInfoPointer  &p=0xc000006040
		&{mm 102 20}
		SetInfoValue  &p=0xc00004c500
		{mm 102 20}

	*/
}
