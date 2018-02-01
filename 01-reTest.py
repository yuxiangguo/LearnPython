#coding=utf-8

import re

#mactch 从头开始匹配
result1 = re.match("itcast", "itcast.cn")
print("result1:%s"%result1.group())
# . 可以匹配任何单个字符，除\n
ret = re.match(".", "a")
print("ret:%s"%ret.group())
# 需要区分大小写
ret1 = re.match("h", "hello Python").group()
print("ret1:%s"%ret1)
ret2 = re.match("H", "Hello Python").group()
print("ret4:%s"%ret2)
#[hH]提取其中的任意一个与字符串第一个字符匹配
ret3 = re.match("[hH]", "hello Python").group()
print("ret3:%s"%ret3)
ret4 = re.match("[hH]", "Hello Python").group()
print("ret4:%s"%ret4)
#0-9写法，[]中的“-”代表一个范围
ret5 = re.match("[0123456789]", "4hello").group()
print("ret5:%s"%ret5)
ret6 = re.match("[0-9]", "4hello").group()
print("ret6:%s"%ret6)
#\d可代表一个数字
ret7 = re.match("嫦娥1号","嫦娥1号发射成功").group()
print("ret7:%s"%ret7)
ret8 = re.match("嫦娥\d号","嫦娥1号发射成功").group()
print("ret8:%s"%ret8)
#在字符串前面加上r表示原生字符串
ret9 =re.match(r"c:\\a", "c:\\a\b\c").group()
print("ret9:%s"%ret9)