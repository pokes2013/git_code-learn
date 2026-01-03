//变量的申明及调用

public class item {
    public static void main(String[] args) {
        //变量在申明前必须指明变量的数据类型
        String name = "亦良";
        System.out.println(name);
        int age = 30;
        System.out.println(age);
        //变量的应用
        System.out.println(name + "今年" + age + "岁了");  //这里使用了一个字符串拼接


        //变量的交换
        int a = 10;
        int b = 20;
        int c = a;  // 将 a 的值赋值给 c
        a = b; // 将 b 的值赋值给 a (原值会覆盖)
        b = c; // 将 c (原 a 的值) 赋值给 b
        System.out.println("a: " + a + ", b: " + b);  // a: 20, b: 10

    }
}




