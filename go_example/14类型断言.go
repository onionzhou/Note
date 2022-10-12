package main

import (
	"fmt"
)

// 鸭子类型， 不关心你是不是鸭子， 只要你的行为像鸭子就是鸭子
type Student struct {
	name string
	id   int
}

func main() {
	i := make([]interface{}, 3)
	i[0] = 10
	i[1] = "hello world "
	i[2] = Student{"tom", 12}

	// 类型查询 类型断言
	// 第一个返回下标，第二个返回下标对应的值，data分别是i[0],i[1],i[2]
	// if  方式
	for index, data := range i {
		//第一个返回的是值，第二个返回判断结果的真假
		if value, ok := data.(int); ok == true {
			fmt.Printf("x[%d] 类型为int,内容为%d\n", index, value)
		} else if value, ok := data.(string); ok == true {
			fmt.Printf("x[%d] 类型为string,内容为%s\n", index, value)
		} else if value, ok := data.(Student); ok == true {
			fmt.Printf("x[%d] 类型为student,内容为 name =%s,id = %d \n", index, value.name, value.id)
		}
	}

	// swtich  方式
	for index, data := range i {
		//第一个返回的是值，第二个返回判断结果的真假
		switch value := data.(type) {
		case int:
			fmt.Printf("x[%d] 类型为int,内容为%d\n", index, value)
		case string:
			fmt.Printf("x[%d] 类型为string,内容为%s\n", index, value)
		case Student:
			fmt.Printf("x[%d] 类型为student,内容为 name =%s,id = %d \n", index, value.name, value.id)

		}
	}

}
