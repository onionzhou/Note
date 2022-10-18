package main

import (
	"fmt"
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
	go NewTask()

	i := 0
	for {
		i++
		fmt.Printf("main task  delay %d\n", i)
		time.Sleep(1 * time.Second)

	}

}
