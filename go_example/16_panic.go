package main


//panic  可以理解为 python rasie  抛异常

func test(x int){
	var a [10]int
	a[x] =10

}
func main(){

	panic("hello world  exit") //panic: hello world  exit

	//test(20)  //panic: runtime error: index out of range [20] with length 10

}