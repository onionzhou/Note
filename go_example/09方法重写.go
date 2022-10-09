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
	id     int
	addr   string
}

// student 也实现了一个方法，这个方法和Person  方法同名， 叫方法重写
func (tmp *Student) PrintInfo() {
	fmt.Printf("name=%s,sex=%c,age=%d\n", tmp.name, tmp.sex, tmp.age)
	fmt.Println("student : tmp  = ",tmp)
}

func main() {

	s := Student{Person{"onion", 'm', 18}, 'a', "bj"}
	s.PrintInfo() // 方法是Person
	/*
	name=onion,sex=m,age=18
	student : tmp  =  &{{onion 109 18} 97 bj}
	*/
	s.Person.PrintInfo() //显示调用Person
}
