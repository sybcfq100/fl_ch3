#! python 3
# phoneAndEmail.py

import pyperclip, re
phoneRegex = re.compile(r'''(
(\d{3}|(\d{3}))?  # area code 因为区号可能只是3 个数字（即\d{3}），或括号中的3 个数字（即\(\d{3}\)），所以应该用管道符号连接这两部分。
(\s|-|\.)?        # separator 电话号码分割字符可以是空格（\s）、短横（-）或句点（.），所以这些部分也应该用管道连接
\d{3}             # first 3 digits
(\s|-|\.)         # separator
\d{4}             # last 4 digits
(\s*(ext|x|ext.)\s*\d{2,5})?  # extension 最后的部分是可选的分机号，包括任意数目的空格，接着ext、x 或ext.，再接着2 到5 位数字。
)''',re.VERBOSE)
# todo: create email regex
emailRegex = re.compile(r'''(
[a-zA-Z0-9._%+-]+  # username 一个或多个字符包括：小写和大写字母、数字、句点、下划线、百分号、加号或短横
@                  # @ symbol
[a-zA-Z0-9.-]+     # domain name 允许的字符分类要少一些，只允许字母、数字、句点和短横：[a-zA-Z0-9.-]。
(\.[a-zA-Z]{2,4})  # dot`something “dot-com”部分（技术上称为“顶级域名”），它实际上可以是“dot-anything”。它有2 到4 个字符
)''', re.VERBOSE)

# find matches in clipboard text
text = str(pyperclip.paste())
matches = [] #将所有的匹配保存在名为matches 的列表变量中
for groups in phoneRegex.findall(text):
	phoneNum = '-',join([groups[1],groups[3],groups[5]]) # 提取数字，按照统一格式存储
	if gourps[8] != '': # 如果第八组
		phoneNum += ' x' + groups[8]
	matches.append(phoneNum)
	
for groups in emailRegex.findall(text):
	matches.append(groups[0])
# copy results to the clipboard
if len(matches) >0:
	pyperclip.copy('\n'.join(matches))
	print('Copied to clipboard:')
	pring('\n'.join(matches))
else:
	print('No phone numbers or email addresses found.')
