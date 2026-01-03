public class 条件语句 {
    public static void main(String[] args) {
        //if大于小于判断
        int x = 10;
        if (x < 20) {
            System.out.print("这是 if 语句");
        }
        //if...else语句
        if (x < 20) {
            System.out.print("这是 if 语句");
        } else {
            System.out.print("这是 else 语句");
        }

        //if...else if...else 语句

        if (x == 10) {
            System.out.print("Value of X is 10");
        } else if (x == 20) {
            System.out.print("Value of X is 20");
        } else if (x == 30) {
            System.out.print("Value of X is 30");
        } else {
            System.out.print("这是 else 语句");
        }

    }
}
