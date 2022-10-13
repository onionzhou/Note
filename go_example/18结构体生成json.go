package main

import (
	"encoding/json"
	"fmt"
)

// 成员变量首字母必须大写

//type IT struct {
//	Company string
//	Subject []string
//	Isok    bool
//	Price   float64
//}

type IT struct {
	Company string `json:"-"` //此字段不会输出屏幕
	Subject []string `json:"subject"`  //二次编码， 输出一个小写的subject
	Isok    bool   `json:",string"`
	Price   float64
}

func main() {
	s := IT{"sx", []string{"go", "c", "python"}, true, 77.77}

	buf, err := json.Marshal(s)
	//buf, err := json.MarshalIndent(s, "", " ") //格式输出json
	fmt.Println(err)
	if err != nil {
		fmt.Println(err)
		return
	}

	fmt.Println(buf)
	fmt.Println(string(buf))
	//{"Company":"sx","Subject":["go","c","python"],"Isok":true,"Price":77.77}

	//{"subject":["go","c","python"],"Isok":"true","Price":77.77}
}
