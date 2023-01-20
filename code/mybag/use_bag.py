import my_bag.file_util
import my_bag.str_util

#反转字符串
str=input("输入字符串")
print(my_bag.str_util.str_reverse(str))

#切片
str=input("输入字符串")
x=int(input("输入首下标"))
y=int(input("输入尾下标"))
print(my_bag.str_util.substr(str,x,y))

#打印文件内容
name=input("输入文件名")
my_bag.file_util.print_file_info(name)

#追加写入数据到文件
str=input("输入字符串")
name=input("输入文件名")
my_bag.file_util.append_to_file(name,str)