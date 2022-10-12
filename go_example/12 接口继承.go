package main

import (
	"fmt"
)

// 鸭子类型， 不关心你是不是鸭子， 只要你的行为像鸭子就是鸭子

type Humer interface { //子集
	sayhello() // 方法只声明， 没有实现，由别的类型(自定义类型)实现
}

type Personer interface { //超集
	Humer
	sing(name string)
}

type Student struct {
	name string
	id   int
}

//student 实现此方法
func (tmp *Student) sayhello() {
	fmt.Printf("name = %s , id = %d \n", tmp.name, tmp.id)
}

func (tmp *Student) sing(name string) {
	fmt.Printf("name = %s , sing =%s  \n", tmp.name, name)
}

func main() {

	var i Personer //
	s := &Student{"kk", 666}
	i = s
	i.sayhello()
	i.sing("hello")
	/*
	name = kk , id = 666
	name = kk , sing =hello
	*/



}
