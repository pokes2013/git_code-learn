public class 增强for循环 {
    public static void main(String[] args) {
        int[] numbers = {10, 20, 30, 40, 50};

        for (int x : numbers) {
            System.out.print(x);
            System.out.print(",");
        }
    //为了方便观看这里添加一个换行
    System.out.print("\n---------------------------\n");

        String[] names = {"James", "Larry", "Tom", "Lacy"};
        for (String name : names) {
            System.out.print(name);
            System.out.print(",");

        }
    }
}
