public class yunsuan {
    public static void main(String[] args) {

        int c = 123;
        String d = "hello";
        System.out.println(c + d);  // 123 + hello = 123hello

        int a = 20, b = 10;
        System.out.println(a + b);  // 10 + 20 = 30

        System.out.println(a - b); // 减法
        System.out.println(a * b); // 乘法
        System.out.println(a / b); //除法
        System.out.println(a % b); //取余

        //递增
        // 第一种先加在赋值
        int a = 1;
        System.out.println(++a); // 2;

        // 第二种先赋值在加
        int b = 1;
        System.out.println(b++); // 1


        //递减
        // 第一种先减在赋值
        int a = 1;
        System.out.println(--a); // 0;

        // 第二种先赋值在减
        int b = 1;
        System.out.println(b--); // 1
    }
}
