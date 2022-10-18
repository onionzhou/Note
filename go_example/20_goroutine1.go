package main

import (
	"fmt"
	"runtime"

	//"runtime"
	"time"
)

func NewTask() {
	i := 0
	for {
		i++
		fmt.Printf("new task  delay %d\n", i)
		time.Sleep(1 * time.Second)

	}
}

func main() {

	go func(s string) {
		for i := 0; i < 2; i++ {
			fmt.Println(s)
			runtime.Goexit() // 直接退出goroutine
		}
	}("hello")
	for i := 0; i < 2; i++ {

		//time.Sleep(1*time.Second)
		runtime.Gosched() //让出cpu 时间片
		fmt.Println("world")
	}

}
