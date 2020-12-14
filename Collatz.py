# -*- coding: utf-8 -*-
"""
@Time        : 2020/11/1
@Author      : sybcf
@File        : Collatz
@Description : 
"""


def Collatz(number):
    if number % 2 == 0:
        num = number // 2
        print(num)
    else:
        num = 3 * number + 1
        print(num)
    return num


try:
    number = int(input())
    while number != 1:
        number = Collatz(number)
        # continue
except:
    print('int are allowed only!')
