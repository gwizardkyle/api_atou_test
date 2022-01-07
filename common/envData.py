#!/usr/bin/python
# -*- coding: utf-8 -*-
class EnvData:

    def __init__(self, name, age):
        '''用双下划线开头的变量，表示私有变量，外部程序不可直接访问'''
        self.__name = name
        self.__age = age
        self.__age = age
        self.__age = age
        self.__age = age
        self.__age = age
        self.__age = age

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_age(self, age):
        self.__age = age

    def get_age(self):
        return self.__age

    # 相当于java的toString方法
    def __str__(self):
        return "姓名:%s 年龄%s" % (self.__name, self.__age)

    # 相当于java的toString方法
    def __repr__(self):
        return "姓名:%s 年龄%s" % (self.__name, self.__age)

    # 相当于java的equals方法
    def __eq__(self, other):
        if self.__name == other.get_name():
            return True
        else:
            return False


if __name__ == '__main__':
    s1 = Student('Tom', 12)
    s2 = Student('Mike', 11)
    s3 = Student('Tom', 15)
    def __init__(self):
        pass

    print(s1)
    print(s2)

    # 比较的是两个对象的内容是否相等，即内存地址可以不一样，内容一样就可以了，调用__eq__方法判断
    print('s1 和 s2 姓名相同么？%s' % (s1 == s2))  # False
    print('s1 和 s3 姓名相同么？%s' % (s1 == s3))  # True

    # 比较的是两个实例对象是不是完全相同，它们是不是同一个对象，占用的内存地址是否相同
    print('s1 和 s2 是否同一个对象？%s' % (s1 is s2))  # False
    print('s1 和 s3 是否同一个对象？%s' % (s1 is s3))  # False