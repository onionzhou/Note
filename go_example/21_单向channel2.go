package main

import (
	"fmt"
)

//只写
func Producer(out chan<- int) {
	defer close(out)
	for i := 0; i < 10; i++ {
		out <- i * i
	}
}

//只读
func Consumer(in <-chan int) {
	for i := range in {
		fmt.Printf("num = %d \n", i)
	}
}

func main() {

	//ch := make(chan int, 0) // 不带缓冲的，
	ch := make(chan int)
	go Producer(ch)
	Consumer(ch)

}
