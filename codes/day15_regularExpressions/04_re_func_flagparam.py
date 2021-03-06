"""
    修饰符 - 可选标志
    概念
    正则表达式可以包含一些可选标志修饰符来控制匹配的模式。修饰符被指定为一个可选的标志
    多个标志可以通过按位 OR(|) 它们来指定
    re.I 忽略大小写
    re.I	使匹配对大小写不敏感
    re.L	做本地化识别（locale-aware）匹配
    re.M	多行匹配，影响 ^ 和 $
    re.S	使 . 匹配包括换行在内的所有字符
    re.U	根据Unicode字符集解析字符。这个标志影响 \w, \W, \b, \B.
    re.X	该标志通过给予你更灵活的格式以便你将正则表达式写得更易于理解。
"""
import re

'''
    特别注意：原始字符串，对正则表达式的匹配影响非常大，
'''
# 原始字符串
str_regx = r'PythonGolang\n93u49s93ndfronger'
print(str_regx)
# 练习1：忽略大小写，返回Python
result = re.findall(r'python', str_regx, re.I)
print(result)  # ['Python']

# 练习2： 输出包括换行符\n在内的字符串，返回Python
result = re.findall(r'Golang.{1}', str_regx, re.S)
print(result)  # ['Golang\\']  why??

# 不是原始字符串
str_regx = 'PythonGolang\n93u49s93ndfronger'
print(str_regx)  # PythonGolang   字符串换行显示了
# 93u49s93ndfronger
result = re.findall(r'python', str_regx, re.I)
print(result)  # ['Python']

result = re.findall(r'Golang.{1}', str_regx, re.S)
print(result)  # ['Golang\n']   输出了\n
