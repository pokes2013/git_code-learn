package 构造器;

//创建一个学生类


import com.sun.org.apache.xalan.internal.xsltc.compiler.util.MatchGenerator;

public class Student {
    private String name;
    private int age;


    //默认的构造器，默认不显示
    public Student() {}

    //自定义构造器
    public Student(String name,int age) {
        this.name = name;
        this.age = age;
    }

    public void show() {
        System.out.println(name + "," + age);
    }

}
