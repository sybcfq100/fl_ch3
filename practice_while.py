'''
current_number = 1
while current_number <=5:
	print(current_number)
	current_number += 1
'''	
'''
active = True
while active:
	message = input('prompt:>')
	 
	if message == 'quit':
		active = False
	else:
		print(message)
'''

'''
prompt = "\nPlease enter the name of a city you have visited: "
prompt += "\n(Enter 'quit' when you are finished.)"
 
 
while True:
	city = input(prompt)
	
	if city == 'quit':
		break
	else:
		print("I'd love to go to " + city.title() +'!')
'''

'''
current_number = 0
while current_number < 10:
	current_number += 1
	if current_number %2 == 1:
	    continue
	    
	print(current_number)
'''
'''
unconfirmed_users = ['alice','brain','candace']
confirmed_users = []
while unconfirmed_users:
	current_user = unconfirmed_users.pop()
	print("Verifying user: " + current_user.title())
	confirmed_users.append(current_user)
print("\nThe following users have been confirmed: ")
for confirmed_user in confirmed_users:
	print(confirmed_user.title())
'''

responses = {}
polling_active = True

while polling_active:
	name = input('\nWhat is your name?')
	response = input('Which mountain do you like?')
	responses[name] = response
	repeat = input('Would you like to let another one respond? (yes/no)')
	if repeat == "no":
		polling_active = False
		
print('n\------ Polling Results ------')
for name, response in responses.items():
	print(name.title() + " would like to climb " + response.title() + '.')
