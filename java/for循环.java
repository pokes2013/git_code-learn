public class for循环 {
    public static void main(String[] args) {
//        for (int x = 10; x < 20; x = x + 1) {
//            System.out.print("X值为:" + x);
//            System.out.print("\n");
//        }

        int[] numbers = {10, 20, 30, 40, 50};

        for (int x : numbers) {
            System.out.print(x);
            System.out.print(",");
        }


    }
}
