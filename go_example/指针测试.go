package main

import "fmt"

func swap(a, b *int) {
	*a, *b = *b, *a
}

func main() {
	aa := 10
	bb := 20
	swap(&aa, &bb)
	fmt.Printf("a =%d ,b=%d \n ", aa, bb)

	var a int = 10
	fmt.Printf("a = %d \n", a)
	fmt.Printf("a = %v \n", &a)

	var p *int
	p = &a
	fmt.Printf("*p = %d \n", *p)
	fmt.Printf("p = %v \n", p)

	p = new(int)
	*p = 2321
	fmt.Printf("*p = %d \n", *p)
	fmt.Printf("p = %v \n", p)

}
