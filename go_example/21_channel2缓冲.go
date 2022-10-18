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

	//ch := make(chan int, 0) // 不带缓冲的，
	ch := make(chan int, 3) //带缓冲的

	fmt.Printf("main len(ch) =%d,cap(ch)= %d\n", len(ch), cap(ch))

	go func() {
		defer  fmt.Println(" 子协程序结束....")
		for i := 0; i < 5; i++ {
			fmt.Printf("子协程=%d\n", i)
			ch <- i
			fmt.Printf("len(ch) =%d,cap(ch)= %d\n", len(ch), cap(ch))
		}
	}()
	//var num int

	time.Sleep(2 * time.Second)
	for i := 0; i < 5; i++ {
		num := <-ch
		fmt.Printf("num = %d \n", num)
	}

}
