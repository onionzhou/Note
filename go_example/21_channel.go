package main

import (
	"fmt"
	"time"
)

func Print(s string) {
	for _, data := range s {
		fmt.Printf("%c", data)
		time.Sleep(1 * time.Second)
	}
	fmt.Printf("\n")
}

func Person1() {
	Print("hello")
	ch <- 111
}

func Person2() {
	<-ch //从管道里取数据，没有数据就会阻塞
	Print("world")

}

var ch = make(chan int)

func main() {

	//b := make(chan int)
	//go func() {
	//	defer fmt.Println("子携程结束")
	//	fmt.Println("子协成doing...")
	//	b <- 125
	//}()
	////var num int
	//num := <- b //从b中接收数据
	//fmt.Println(num)
	//fmt.Printf("%T\n",num)
	//fmt.Println("main end!!")

	go Person1()
	go Person2()
	fmt.Println("main end!!")
	for {

	}

}
