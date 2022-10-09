package main

import "fmt"

func main() {
	var m1 map[int]string

	fmt.Println("m1 = ", m1)
	fmt.Println("len =  ", len(m1))

	m2 := make(map[int]string, 2)
	fmt.Println("m2 = ", m2)
	fmt.Println("len =  ", len(m2))
	m2[11] = "h11"
	m2[12] = "h12"
	m2[13] = "h13"
	fmt.Println("modify m2 =  ", m2)
	fmt.Println("len = ", len(m2))

	m4 := map[int]string{1: "h1", 2: "h2"}
	fmt.Println(m4)
	/*
		m1 =  map[]
		len =   0

		m2 =  map[]
		len =   0

		modify m2 =   map[11:h11 12:h12 13:h13]
		len =  3

		map[1:h1 2:h2]
	*/

	// 遍历

	m5 := map[int]string{1: "h1", 2: "h2"}

	for k, v := range m5 {
		fmt.Printf(" %d ===> %s \n", k, v)
		/*
			result
			 1 ===> h1
			 2 ===> h2
		*/
	}

	// 删除m5 key 为 1 的值
	delete(m5, 1)
}
