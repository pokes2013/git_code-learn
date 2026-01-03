# 实战二：使用列表存储学生信息

"""
- 题目：定义学生类录入5个学生信息存储到列表中
- 需求：定义学生类Student，包含姓名、年龄、性别、分数四个属性，提供一个用于学员信息输出的方法info(self)。
        使用循环录入5位学生的信息，由于录入的学生信息中间使用“#”进行分隔，
        所以需要使用字符串的`split()`方法，进行分割，使用分割的信息创建学生对象，
        使用列表存储学生信息，最后使用循环遍历列表，调用对象的`info()`方法输出学员信息。
- 结果类似：
        我的名字叫小美,今年20岁了,我是女生,我的成绩是99分
        我的名字叫小红,今年20岁了,我是女生,我的成绩是85分
        我的名字叫小明,今年20岁了,我是男生,我的成绩是85分
        我的名字叫小刚,今年20岁了,我是男生,我的成绩是81分
        我的名字叫小佳,今年20岁了,我是男生,我的成绩是60分

"""

class Student:

    # score 分数，成绩

    def __init__(self, name, age, gender, score):
        self.name = name
        self.age = age
        self.gender = gender
        self.score = score

    def info(self):
        print(f"我的名字叫{self.name},今年{self.age}岁了,我是{self.gender}生,我的成绩是{self.score}分")


if __name__ == "__main__":
    print("请输入五位学生信息：姓名#年龄#性别#成绩")
    stu_list = []
    for i in range(1, 6):
        s = input(f"请输入第{i}位学生的信息:")

        s_list = s.split("#")  # 这一步的结果是：['小美', '20', '女', '95']，他是一个list

        # 既然是一个list，那么我们可以通过下标切片：姓名，s_list[0]，年龄s_list[1]，性别s_list[2]，分数s_list[3]
        # 传参：stu=Student(s_list[0],s_list[1],s_list[2],s_list[3])

        # 创建学生对象
        stu = Student(s_list[0], s_list[1], s_list[2], s_list[3])
        stu_list.append(stu)

    for item in stu_list:
        item.info()
