'''
import re


heroRegex = re.compile(r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey.')
print(mo1. group())

mo2 = heroRegex.search('Tina Fey and Batman.')
print(mo2. group())

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel.')
print(mo.group())
print(mo.group(1))


batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group())

mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())


phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo1 = phoneRegex.search('My number is 415-555-4242')
print(mo1.group())
mo2 = phoneRegex.search('My number is 555-4242')
print(mo2.group())


import re
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4242.')
print(mo.group(1))
print(mo.group(2))
print(mo.group(0))
print(mo.group())
print(mo.groups())
areaCode, mainNumber = mo.groups()
print(areaCode)
print(mainNumber)


import re


batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group())
# 'Batman'
mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())
# 'Batwoman'
mo3 = batRegex.search('The Adventures of Batwo and Batwomen and Batwowowowoman')
print(mo3.group()) 

import re


batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The Adventures of Batwoman')
mo2 = batRegex.search('The wo Adventures of Bat wo man')
mo3 = batRegex.search('The Adventures of Batman')
print(mo1)
print(type(mo1))
print(mo1.group())
print(mo2)
pri
nt(mo3)

import re

greedyHaRegex = re.compile(r'(Ha){3,5}')
mo1 = greedyHaRegex.search('HaHaHaHaHaHa')
print(mo1.group())
nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
mo2 = nongreedyHaRegex.search('HaHaHaHaHaHa')
print(mo2.group())


import re


vowelRegex = re.compile(r'[^aeiouAEIOU.]')
vowelRegex.findall('RoboCop eats baby food. BABY FOOD.')
print(vowelRegex.findall('RoboCop eats baby food. BABY FOOD.'))


import re
noNewlineRegex = re.compile('.*')
noNewlineRegex.search('Serve the public trust. \nProtect teh innovent.\nUphold the law.').group()
print(noNewlineRegex.search('Serve the public trust. \nProtect teh innovent.\nUphold the law.').group())

newlineRegex = re.compile('.*',re.DOTALL)
newlineRegex.search('Serve the public trust. \nProtect teh innovent.\nUphold the law.').group()
print(newlineRegex.search('Serve the public trust. \nProtect teh innovent.\nUphold the law.').group())

import re
agentNamesRegex = re.compile(r'Agent (\w)\w*')
mo = agentNamesRegex.findall('Agent Alice told Agent Carol that Agent Eve knew Agent ' \
 + 'Bob was a doubnel agent.')
mo1 = agentNamesRegex.sub(r'\1****','Agent Alice told Agent Carol that Agent Eve knew Agent ' \
 + 'Bob was a doubnel agent.' )
print(mo)
print(mo1)
'''
import re
phoneRegex = re.compile(r'''( \n
                        (\d{3}|(\d{3}\))?  \n # area code"  
                        (\s|-|\.)?        \n # separator" 
                        (\d{3})            \n # first 3 digits" 
                        (\s|-|\.)      \n   # separator" 
                        (\d{4})        \n     # last 4 digits" 
                        (\s*(ext|x|ext.)\s*\d{2,5}))?  \n # extension" 
                        )''', re.VERBOSE)
text = 'My number is 415-555-4242 and email sybcfq100@gmail.com.'
mo = phoneRegex.findall(text)
print(mo)

'''
matches = []
for groups in phoneRegex.findall(text):
	phoneNum = '-'.join([groups[1],groups[3],groups[5]]) # 提取数字，按照统一格式存储
	if groups[6] != '': # 如果第八组
		phoneNum += ' x' + groups[8]
	matches.append(phoneNum)
if len(matches) >0:
	print('Copied to clipboard:')
	print('\n'.join(matches))
else:
	print('No phone numbers or email addresses found.')
'''
