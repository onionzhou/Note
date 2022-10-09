package main

import "fmt"

// 鸭子类型， 不关心你是不是鸭子， 只要你的行为像鸭子就是鸭子

type Humer interface {
	sayhello() // 方法只声明， 没有实现，由别的类型(自定义类型)实现
}

type Student struct {
	name string
	id   int
}

//student 实现此方法
func (tmp *Student) sayhello() {
	fmt.Printf("name = %s , id = %d \n", tmp.name, tmp.id)
}

type Teacher struct {
	name string
	id   int
	addr string
}

//Teacher 实现此方法
func (tmp *Teacher) sayhello() {
	fmt.Printf("name = %s , id = %d  addr = %s \n", tmp.name, tmp.id, tmp.addr)
}

type Mystr string

func (tmp *Mystr) sayhello() {
	fmt.Printf("Mystr = %s , p = %p \n", *tmp, tmp)
}

func main() {

	var i Humer
	s := &Student{"kk", 666}
	i = s
	i.sayhello()

	t := &Teacher{"kk", 666, "bj"}
	i = t
	i.sayhello()

	var s1 Mystr = "hello world"
	i = &s1
	i.sayhello()

	/*
		name = kk , id = 666
		name = kk , id = 666  addr = bj
		Mystr = hello world , p = 0xc00004a280

	*/

}
