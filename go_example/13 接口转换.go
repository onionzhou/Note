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

	//  超集可以转换为子集， 反过来不行
	var ipro Personer // 超集
	var i Humer       // 子集
	ipro = &Student{"kk", 666}
	i = ipro
	//ipro = i  err
	i.sayhello()

	/*
		name = kk , id = 666
	*/

}
