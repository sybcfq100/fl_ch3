# -*- coding: utf-8 -*-
"""
@Time        : 29/11/2020
@Author      : sybcf
@File        : 2Dvector
@Description : 
"""
'''
from math import hypot


class Vector:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Vector(%r, %r)' % (self.x, self.y)

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)


metro_areas = [
    ['Tokyo', 'JP', 36.933, (35.689722, 139.691667)],
    ['Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)],
    ['Mexico City', 'MX', 20.142, (19.433333, -99.133333)],
    ['New York-Newark', 'US', 20.104, (40.808611, -74.020386)],
    ['Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)],
]

print('{:15} | {:^9} | {:^9}'.format('', 'lat.', 'long.'))
fmt = '{:15} |{:9.4f} | {:9.4f}'
for name, cc, pop, (latitude, longitude) in metro_areas:
    if longitude <= 0:
        print(fmt.format(name, latitude, longitude))


import bisect
import sys

HAYSTACK = [1, 4, 5, 6, 7, 12, 15, 20, 21, 23, 23, 26, 29, 30]
NEEDLES = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]

ROW_FMT = '{0:2d} @ {1:2d}    {2}{0:<2d}'  # 第一个参数，宽度2个字符；@；第二个参数，宽度2分字符；空格；第三个参数；第一个参数，宽度2个字符，左对齐


# 函数的作用：
def demo(bisect_fn):
    for  needle in reversed(NEEDLES): # 反向插入needle的值，第一个是31、
    # for needle in NEEDLES:
        position = bisect_fn(HAYSTACK, needle)# 利用bisect函数计算元素应该出现的位置
        offset = position * '  |' #利用该位置计算出需要几个分割符号
        print(ROW_FMT.format(needle, position, offset)) # 把元素和其应该出现的位置打印出来


if __name__ == '__main__':
    if sys.argv[-1] == 'left':
        bisect_fn = bisect.bisect_left
    else:
        bisect_fn = bisect.bisect

    print('DEMO: ', bisect_fn.__name__)
    print('haystack ->', ' '.join('%2d' % n for n in HAYSTACK))
    demo(bisect_fn)
'''
import bisect
import random


SIZE = 7
random.seed(19)
my_list = []
for i in range(SIZE):
    new_item = random.randrange(SIZE*2)
    bisect.insort(my_list, new_item)
    print('%2d ->' % new_item, my_list)