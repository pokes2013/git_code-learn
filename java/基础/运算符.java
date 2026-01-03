public class 运算符 {
    public static void main(String[] args) {
        int a = 2;
        int b = 3;
        int c = 4;
        int d = 5;
        int e = 6;


        System.out.println(a + b);
        System.out.println(a - b);
        System.out.println(a * b);
        System.out.println(e / b);

        //5除以3得值是浮点型，必须转为浮点型，负责不准确
        System.out.println(d / (double) b);


    }
}
