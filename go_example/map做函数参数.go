package main

import "fmt"

func test(m map[int]string) {

	delete(m, 1)

}

func main() {

	m := map[int]string{1: "h1", 2: "h2"}
	fmt.Println("m = ", m)
	test(m)
	fmt.Println("m = ", m)
	/*
		操作的是同一个map
		m =  map[1:h1 2:h2]
		m =  map[2:h2]

	*/


}
