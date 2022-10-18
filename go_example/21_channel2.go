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


func main() {

	b := make(chan int)
	go func() {
		defer fmt.Println("子携程结束")
		fmt.Println("子协成doing...")
		Print("hello")
		b <- 125
	}()
	//var num int
	num := <- b //从b中接收数据
	fmt.Println(num)
	fmt.Printf("%T\n",num)
	fmt.Println("main end!!")
	/*
	子协成doing...
	hello
	子携程结束
	125
	int
	main end!!
	*/


}
