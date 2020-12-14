'''
filename = 'programming.txt'
with open(filename,'w') as file_object:
	file_object.write("I love progarmming.\n")
with open(filename,'a') as file_object:
	file_object.write("I also love finding meaning in large datasets.\n")
	
'''

'''
filename = 'guest.txt'
with open(filename,'a') as file_object:
	active = True
	while active:
		name = input('please enter your name > :')
		if name == 'ok':
			active = False
		else:
			file_object.write('welcome! ' + name.title() + '\n')
'''

print('Give me two numbers, and I will  divide them.')
print("enter 'q' to quit")
while True:
	first_number = input('\nFirst number:')
	if first_number == 'q':
		break
	second_number = input('\nSecond number:')
	try:
		answer = int(first_number)/int(second_number)
	except ZeroDivisionError:
		print("You can't divide by 0")
	else:
		print(answer)
