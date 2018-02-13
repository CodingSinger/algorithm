# -*- coding: UTF-8 -*-
#python 关于 for循环 命名空间和变量作用域的一个疑问？ - 知乎用户的回答 - 知乎
# https://www.zhihu.com/question/22466764/answer/21464993


def sum():



    list2 = [2,3,4,5,6]
    print list2[-1]

    print list2[-1]
    p = "d"
    print p.split()[-1]

    if p == None:
        print "Nonbe"

    if p:
        print "非空"
    else:
        print "空"

    str ="dsd"
    print str[0:1]

    for i in range(10):
        print i
    l = []

    if l:
        print "ss"
    else:
        print "dsd"
    s = "ss"
    print s[1]
    for n in range(2,10):
        print n

    #为什么python在for循环外还能使用for循环里的变量 在java c go等 中大多数语言是不可以的 可以理解成Python其实没有for的变量作用域这个概念
    # python中的变量作用域 ：本地作用域（Local）→当前作用域被嵌入的本地作用域（Enclosing locals）→全局/模块作用域（Global）→内置作用域（Built-in）
    # for中的变量也被包括在本地作用域范围中


    x = 10
    i = 0
    while i <9:
        x = i
        i = i+1
    print x


sum()