"""
    一、什么是变量作用域呢？
       在维基上给出的定义是“The scope of a variable describes where in a program's text the variable may be used,
       while the extent (or lifetime) describes when in a program's execution a variable has a (meaningful) value.
      ”简而言之就是两点，在何处可以使用变量以及标识符绑定的值生存多久。
    二、LEGB原则：Python的作用域规则最出名的就是LEGB，这四个字母的含义代表着Python的对于变量的查找顺序：
       locals -> enclosing -> globals -> builtins。
    
    三、在函数内部定义的局部变量只是在该函数内可见，当函数运行结束后，在其内部定义的所有局部变量将被自动删除且不可访问。
       在函数内部使用global定义的全局变量，当函数结束以后人然存在并且可以访问

       局部变量的空间是在栈上分配的，而栈空间是由操作系统维护的，每当调用一个函数时，操作系统会为其分配一个栈帧，函数调用结束后立刻释放这个栈帧。
       因此，函数调用结束后，该函数内部所有的局部变量都不再存在
    四、nonlocal变量
       介于局部变量和全局变量之间的变量。关键字nonlocal声明的变量会引用距离最近的非全局作用域的变量，要求声明的变量已存在，关键字不会创建新的变量
    参考：https://www.cnblogs.com/fireporsche/p/7813961.html
"""

'''
    1、Python变量的作用域由变量所在源代码中的位置决定。只有当变量在Module(模块)、Class(类)、def(函数)中定义的时候，
    才会有作用域的概念，并不是所有的语句块都会产生作用域
'''
result = 50


def add(x, y):
    result = x + y;
    print(result)


add(1, 2)  # 3  打印的是def函数中的变量值
print(result)  # 50  而不是3，虽然result名字相同，但是作用域不同。def函数中的变量result在其内部可以访问，其他地方无法访问
# 测试，当注释掉result=50时，结果报错：NameError: name 'result' is not defined

'''
    2、在作用域中定义的变量，一般只在作用域中有效。 需要注意的是：
    在if-elif-else、for-else、while、try-except\try-finally等关键字的语句块中并不会产成作用域。
    看下面的代码：
'''
if True:
    variable = 100
    print(variable)

print("******")
print(variable)
# 结果为：  虽然是在if语句中定义的variable变量，但是在if语句外部仍然能够使用
# 100
# ******
# 100

'''
    3、作用域的类型
'''

# 1、L(local)局部作用域  定义在函数def内的变量

# 2、E(enclosing)嵌套作用域  这个是相对于局部作用域而言的，在实际开发中可能会嵌套定义函数。嵌套作用域是局部作用域的上级def函数内的变量

# 3、G(global)全局作用域  使用global关键字声明的变量
'''
    global关键字在ptyhon中是定义全局变量
    在之前的学习，局部变量很容易会覆盖全局变量的值。
    但是现在有这样一个需求，定义的全局变量要参与业务逻辑，部分函数中会使用全局变量，并改变其的值以供其他函数调用
    在python中可以把局部变量变成全局变量，加global关键字
    
    如果想要在函数内部修改一个定义在函数外的变量值，必须使用global明确声明，否则会自动创建新的局部变量。
    
'''


def demo():
    global a  # 局部变量a变为全局变量
    a = 1
    c = 2


# 函数外部调用c,打印结果
# demo()
# print(c)   #NameError: name 'c' is not defined


# 函数外部调用a,打印结果
demo()
print(a)  # 1

# 4、B(built-in)内置作用域  定义在built-in内置函数、内置模块里的变量

# 练习：作用域链

c = 1


def func1():
    c = 2

    def func2():
        # c = 3
        print(c)

    func2()


func1()

'''
结果为：3     先找Local作用域，发现c = 3 所以打印

注释掉c = 3后，结果为：2   local没有变量，则去找enclosing嵌套作用域

注释掉c = 2后，结果为：1  local和enclosing都没有变量，则去找global全局作用域

'''

'''
    4、nonlocal变量案例
'''


def scope_test():
    def do_local():
        spam = '我是局部变量'

    def do_nonlocal():
        nonlocal spam  # 这时要求spam必须是已经存在的变量
        spam = '我是nonlocal变量'

    def do_global():
        global spam  # 如果全局作用域没有spam，就自动创建一个
        spam = '我是全局变量'

    spam = '原来的值(也是局部变量)'
    do_local()
    print('局部变量赋值后:', spam)
    do_nonlocal()
    print('nonlocal变量赋值后:', spam)
    do_global()
    print('全局变量复制后:', spam)

scope_test()
print('全局变量:', spam)

'''
    运行结果为：
    局部变量赋值后: 原来的值(也是局部变量)
    nonlocal变量赋值后: 我是nonlocal变量
    全局变量复制后: 我是nonlocal变量
    全局变量: 我是全局变量
'''