# -*- coding: utf-8 -*-
"""
@Time        : 10/11/2020
@Author      : sybcf
@File        : removeCsvHeader
@Description : 
"""
# removes the header from all csv files in the current
# woring dirctory
import re
phoneRegex = re.compile(r'''( 
                        (\d{3}|\(\d{3}\))?   # area code"  
                        (\s|-|\.)?         # separator" 
                        (\d{3})             # first 3 digits" 
                        (\s|-|\.)         # separator" 
                        (\d{4})             # last 4 digits" 
                        (\s*(ext|x|ext.)\s*(\d{2,5}))?  # extension" 
                        )''', re.VERBOSE)
# text = 'My number is 415-555-4242 and email sybcfq100@gmail.com.'
mo = phoneRegex.findall('415-555-4242  ext 012 and 415-555-2121')
print(mo)
