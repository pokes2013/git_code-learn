package main

import "fmt"

//定义老师结构体，将老师的各个属性，统一放到结构体中管理
type Teacher struct {

	//属性变量大写，则为公开外界可以访问，小写则为私有属性
	Name   string
	Age    int
	School string
}

func main() {


	//创建老师结构体的实例、对象
	var t1 Teacher
	fmt.Println(t1) //{ 0 } ,未赋值之前的默认值{ 0 }
	t1.Name = "张老师"
	t1.Age = 34
	t1.School = "清华大学"
	fmt.Println(t1) //{张老师 34 清华大学}
	//这里我们调用t1.Name和t1.Age，拼接成一句完整的话
	//需要注意的是不能使用"+"号拼接，t1.Age是整形，不能和字符串拼接
	fmt.Println("十年后"+t1.Name+"的年龄是", t1.Age+10, "岁")  //十年后张老师的年龄是 44 岁

	//方法2:推荐
	var t2 Teacher=Teacher{"王老师",25,"北京大学"}
	fmt.Println(t2)

	//方法3:
	var t3 *Teacher=new(Teacher)
	(*t3).Name="李老师"
	(*t3).Age=33
	(*t3).School="苏州大学"
	fmt.Println(*t3)

}
