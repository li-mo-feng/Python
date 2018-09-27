#!/usr/bin/env python
def w1(func):
    def inner():
        print('...验证权限...')
        func()

    return inner

@w1
def f1():
    print('f1 called')


@w1
def f2():
    print('f2 called')


f1()
f2()