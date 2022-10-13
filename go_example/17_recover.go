package main

import "fmt"

// error  代表普通错误
//panic  可以理解为 python rasie  抛异常 ， 相当于致命错误
// recover  保证发生了panic  程序也能正常执行

func test(x int) {
	//设置recover
	defer func() {
		//recover()
		//打印崩溃信息,如果产生的异常
		if err := recover(); err != nil {
			fmt.Println(err)
		}

	}() //调用匿名函数
	var a [10]int
	a[x] = 10

}
func main() {

	//panic("hello world  exit") //panic: hello world  exit

	test(20) //panic: runtime error: index out of range [20] with length 10

}
