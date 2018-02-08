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

ret10 = re.match('[A-Z][a-z]*', 'Mm').group()
print("ret10:%s"%ret10)
#后面加*号匹配小写字符出现零次或无限次
ret11 = re.match('[A-Z][a-z]*', 'MasasaLLL').group()
print("ret11:%s"%ret11)
# +号代表字母至少匹配一次
ret12 = re.match("[a-zA-Z]+[\w_]*", "name1___22a").group()
print("ret12:%s"%ret12)

ret13 = re.match("[1-9]?[0-9]", "09").group()
print("ret13:%s"%ret13)

ret14 = re.match(r"[\w]{4,20}@163\.com$", "aoi23sdsdsqw22222@163.com").group()
print("ret14:%s"%ret14)
# \b匹配单词的边界
ret15 = re.match(r".*\bver\b", "ho ver abc").group()
print("ret15:%s"%ret15)
# \B 匹配非单词的边界
ret16 = re.match(r".*\Bver\B", "ho verabc").group()
print("ret16:%s"%ret16)

ret17 = re.match(r"([^.]*)-(\d+)", "010-90909090as").group()
print("ret17:%s"%ret17)



