# -*- coding: utf-8 -*-
"""
@Time        : 02/11/2020
@Author      : sybcf
@File        : about_getInDir
@Description : 
"""
import pprint
message = 'it was a bright cold day in April, and the clocks were striking thirteen.'
count = {}
for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1
pprint.print(count)
