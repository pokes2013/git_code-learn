package 构造器;

public class StudentDome {
    public static void main(String[] args) {

        //创建对象
        Student s1 = new Student();
        //直接调用show方法
        s1.show();   //系统默认的构造器  null,0

        Student s2 = new Student("刘德华",30);
        s2.show();    //自定义构造器

    }
}
