package main

import "fmt"

type Person struct {
	name string
	sex  byte
	age  int
}

func (tmp *Person) PrintInfo() {
	fmt.Printf("name=%s,sex=%c,age=%d", tmp.name, tmp.sex, tmp.age)
}


type Student struct {
	Person // 匿名字段
	id int
	addr  string
}

func main(){

	s := Student{Person{"onion",'m',18},'a',"bj"}
	s.PrintInfo() // 方法是Person
	//name=onion,sex=m,age=18

}