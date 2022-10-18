package main

import "fmt"

//ch 只协, quit 只读
func fibonacci(ch chan<- int, quit <-chan bool) {
	// 监听通道
	x, y := 1, 1
	for {
		select {
		case ch <- x:
			x, y = y, x+y
		case flag := <-quit:
			fmt.Println(flag)
			return
		}
	}
}
func main() {
	ch := make(chan int)
	quit := make(chan bool) //判断是否结束

	//消费者 从channel里都数据
	go func() {
		for i := 0; i < 10; i++ {
			num := <-ch
			fmt.Printf("num = %d \n", num)
		}
		quit <- true
	}()

	//生产者
	fibonacci(ch, quit)

}
