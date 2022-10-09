package main

import "fmt"

func main() {

	var a [5]int = [5]int{1, 2, 3, 4, 5}
	fmt.Printf("a = %d\n", a)

	b := [5]int{1, 2, 3, 4, 5}
	fmt.Printf("b = %d\n", b)

	c := [5]int{1, 2, 3}
	fmt.Printf("c = %d\n", c)

	// 数据指定赋值
	d := [5]int{2: 1, 4: 2}
	fmt.Printf("d = %d\n", d)
	/*
		a = [1 2 3 4 5]
		b = [1 2 3 4 5]
		c = [1 2 3 0 0]
		d = [0 0 1 0 2]

	*/

	e := [5]int{1, 2, 3, 4, 5}
	f := [5]int{1, 2, 3, 4, 5}
	g := [5]int{1, 2, 3}
	// 数组比较
	fmt.Println("e == f", e == f)
	fmt.Println("e == g", e == g)
	g[3] = 10
	fmt.Println(g)
	/*
		e == f true
		e == g false
		[1 2 3 10 0]

	*/

}
