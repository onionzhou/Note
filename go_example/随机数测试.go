package main

import (
	"fmt"
	"math/rand"
	"time"
)

func main() {

	//rand.Seed(1) // 种子一样产生的随机数就是一样的
	rand.Seed(time.Now().UnixNano()) //
	fmt.Println(rand.Int())          //7834598577573818367
	fmt.Println(rand.Intn(10))       // 限制数在10 以内
}
