# python和常见的绝大多数语言一样，同样存在值类型和引用类型，在python中也可以称为不可变类型和可变类型
# 1、值类型：对象本身不允许修改，常见的如int、str、tuple
# 另外补充：id() 函数用于获取对象的内存地址。
a = 10
b = a
print(id(a))  # 140727878800704
print(id(b))  # 140727878800704
# 此时改变a的值，看b的值是否改变
a = 20
print(a)  # 20  a的值变了，b的值是否也会发生变化？
print(id(a))  # 140727878801024    a指向的内存地址发生了变化，新开辟了一个内存空间，可见此时a的值变为20
print(id(b))  # 140727878800704
print(b)  # 10                 但是b指向的内存地址并没有发生变化,

# 既然提到了值类型时不可修改的，下面这段代码中，str的值为什么变化了？
str = "hello"
print(str)  # hello
print(id(str))  # 2017452777688
str = str + "world"
print(str)  # helloworld
print(id(str))  # 2572120276656  ,实质上内存地址为2017452777688指向的值并没有改变，之所以str发生了变化，是str新开辟了一个
# 内存空间，将"hellowor"值指向了了这个新的内存地址(2572120276656)中，所以值变了

print("*****************************我是分隔符****************************")
# 2、引用类型：对象本身可以被修改，常见的如list、set、dict
list1 = [1, 2, 3, 4]
list2 = list1
print(id(list1))  # 2985066455624
print(list2)  # [1, 2, 3, 4]
print(id(list2))  # 2985066455624    两个list的内存地址是一致的

list1[0] = 'hello'
print(list2)  # ['hello', 2, 3, 4]

print(id(list1))  # 2985066455624
print(id(list2))  # 2985066455624   虽然list1的值发生了改变，但是其指向的内存地址还是没有变化的，并且两个list的内存地址还是一致的，
# 所以最终结果list1始终是等于list2的
