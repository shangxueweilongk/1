#实现序列反转
def str_reverse(s):
    return s[::-1]

def substr(s,x,y):
    """
    :param s: 传入的字符串
    :param x: 进行切片的首个下标
    :param y: 进行切片末尾的下标
    :return: 返回切片后的字符串
    """
    return s[x:y:]