"""
接收传入文件路径的路径，打印文件全部内容，如文件不存在则捕获异常，
输出提示信息，通过finally关闭文件对象
"""
def print_file_info(file_name):
    try:
        f=open(file_name,"r",encoding="UTF-8")
        print(f.read())
    except:
        print("文件不存在，打开失败")
    finally:
        f.close()


#接收文件路径以及传入数据，将数据追加写入到文件中

def append_to_file(file_name,data):
    try:
        f = open(file_name, "a", encoding="UTF-8")
        f.write(data)
    except:
        print("文件不存在，打开失败")
    finally:
        f.close()
