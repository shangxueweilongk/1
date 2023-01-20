#类的成员方法

class stu:
    name=None
    age=None
    def s(self):
        print("hi")
    def d(self,mes):
        print(mes)
a=stu()
a.name=input("输入名字")
print("--------------")
a.age=input("输入年龄")
print("--------------")
a.d("day day up")
print("--------------")
a.s()