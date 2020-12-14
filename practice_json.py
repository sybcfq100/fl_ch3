import json
'''
numbers = [2,3,5,7,11,13]
filename = 'numbers.json'
with open(filename, 'w') as f_obj:
	json.dump(numbers, f_obj)

filename = 'numbers.json'
with open(filename) as f_obj:
	numbers = json.load(f_obj)
	
print(numbers)
	
'''

filename = 'username.json'
try:
	with open(filename) as f_obj:
		username = json.load(f_obj)
except FileNotFoundError:
	username = input('what is your name?')
	with open(filename,'w') as f_obj:
		json.dump(username, f_obj)
		print('we will remeber you when you come back,' + username + '!')
else:
	print("Welcome back, " + str(username) + '!')
