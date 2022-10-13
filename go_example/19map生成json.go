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
	Company string   `json:"-"`       //此字段不会输出屏幕
	Subject []string `json:"subject"` //二次编码， 输出一个小写的subject
	Isok    bool     `json:",string"`
	Price   float64
}

func main() {
	//s := IT{"sx", []string{"go", "c", "python"}, true, 77.77}

	// 通过map 来生成json
	s := make(map[string]interface{}, 4)
	s["Company"] = "bj"
	s["Subject"] = []string{"go", "c", "c++"}
	s["Isok"] = true
	s["Price"] = 99.999

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

	// 将json 转换为 结构体接收
	itjson := `{"subject":["go","c","python"],"Isok":"true","Price":88.77}`

	var tmp IT
	err  =json.Unmarshal([]byte(itjson),&tmp)
	if err != nil{
		fmt.Println(err)
		return
	}
	fmt.Println(tmp)
	fmt.Printf("tmp2 = %+v\n",tmp)

	// 只接收部分
	type IT2 struct {
		Price   float64
	}
	var tmp2 IT2
	err  =json.Unmarshal([]byte(itjson),&tmp2)
	if err != nil{
		fmt.Println(err)
		return
	}
	fmt.Println(tmp2)
	fmt.Printf("tmp2 = %+v\n",tmp2)
	/*
	{ [go c python] true 88.77}
	tmp2 = {Company: Subject:[go c python] Isok:true Price:88.77}
	{88.77}
	tmp2 = {Price:88.77}
	*/
}
