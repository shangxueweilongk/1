#构造方法
class stu:
    name=None
    age=None

    def __init__(self,name,age):
        self.name=name
        self.age=age

stu1=stu("伍六七",19)
print(stu1.name,stu1.age)

#字符串方法
class stu:
    name=None
    age=None

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __str__(self):
        return f"{self.name},{self.age}"

stu1=stu("伍六七",19)
print(stu1)

#小于符号比较方法
class stu:
    name=None
    age=None

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __lt__(self,other):
        return self.age<other.age

stu1=stu("伍六七",22)
stu2=stu("十三",20)
print(stu1<stu2)
print(stu1>stu2)

#小于等于符号比较方法
class stu:
    name=None
    age=None

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __le__(self,other):
        return self.age<=other.age

stu1=stu("伍六七",20)
stu2=stu("十三",20)
print(stu1<=stu2)
print(stu1>=stu2)

#相等
class stu:
    name=None
    age=None

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __eq__(self,other):
        return self.age==other.age

stu1=stu("伍六七",20)
stu2=stu("十三",20)
print(stu1==stu2)