class A:
	pass

class B:
	pass

# 注意：这里是一个多继承的关系，C类继承了A和B
class C(A,B):    
	def __init__(self,name,age):
		self.name=name
		self.age=age




if __name__ == '__main__':
	a=A() #创建A类的对象
	b=B()
	c=C("小美",20)

	# 查看对象属性，结果是一个字典
	print(a.__dict__)   #a没有添加属性，所以是空的{}
	print(c.__dict__)	#c有三个属性，所以运行结果是：{'name': '小美', 'age': 20}

	# 查看对象所属类
	print(a.__class__)  #运行结果：<class '__main__.A'> ，a属于A这个类的
	print(b.__class__)
	print(c.__class__)

	# 查询类的父类，结果是一个元组
	print(A.__bases__)	#运行结果：(<class 'object'>,)
	print(B.__bases__)	#运行结果：(<class 'object'>,)
	print(C.__bases__)  #运行结果：(<class '__main__.A'>, <class '__main__.B'>)

	# 类的父类，如果是继承多个父类，结果是第一个父类，类型是字符串
	print(A.__base__)  #运行结果：<class 'object'>
	print(C.__base__)  #运行结果：<class '__main__.A'>   因为C继承了AB,如果A在前面则结果是A类，如果B在前面则结果是B类

	#查询继承的关系的途径
	print(A.__mro__)  # A类继承了object类

	print(C.__mro__)  
	# 运行结果：(<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)
	# C类继承了A和B类，AB这两个类又继承了object类

	# 查询子类，结果是一个list
	print(A.__subclasses__())  #运行结果：[<class '__main__.C'>] ，意思是A有一个子类是C
	print(C.__subclasses__())  #C没有子类，所以是空

