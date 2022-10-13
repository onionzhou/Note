package main

import (
	"errors"
	"fmt"
)

func Mydiv(a, b int) (result int, err error) {

	if b == 0 {
		err = errors.New("分母不能为0")

	} else {
		result = a / b
	}
	return
}

func main() {
	var err1 error = errors.New("error is 1")
	fmt.Println(err1)
	var err2 error = fmt.Errorf("error is 2")
	fmt.Println(err2)

	result, err := Mydiv(10, 0)
	if err != nil {
		fmt.Println(err)
	} else {
		fmt.Println(result)
	}

}
