filename = 'pi_digits.txt'
with open(filename) as file_object:
	lines = file_object.readlines()
	
pi_string = ' '
for line in lines:
	pi_string += line.strip()
	

birthday = input("Enter your birthday, in the form mmddyy: ")

if birthday in pi_string:
	print("You are a Pi-Child")
else:
	print("You are not a Pi-Child")

