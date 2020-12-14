'''
def get_formatted_name(first_name, last_name):
	full_name = first_name + ' ' + last_name
	return full_name.title()
	
musican = get_formatted_name('albert', 'Eininsten')
print(musican)
'''
'''
def build_person(first_name, last_name, age = ''):
	person = {'first': first_name, 'last': last_name}
	if age:
		person['age'] = age
	return person
	
musician = build_person('jimi','hendrix',age = 27)
print(musician)
'''

'''
def print_models(unprinted_designs, completed_models):
	while unprinted_designs:
		current_design = unprinted_designs.pop()
		print("Printting model: " + current_design)
		completed_models.append(current_design)
		
def show_completed_models(completed_models):
	print("\nThe following models have been printed:")
	for completed_model in completed_models:
		print(completed_model)
		
unprinted_designs = ['iphone case','robot pendant']
completed_models = []
print_models(unprinted_designs[:],completed_models)
show_completed_models(completed_models)
'''
'''
def make_pizza(*toppings):
	print("\nMaking a pizza with following toppings: ")
	for topping in toppings:
		print('- ' + topping)
	
make_pizza('pepperoni')
make_pizza('mushrooms','green peppers','extra cheese')
'''


def make_pizza(size,*toppings):
	print('\nMaking a '+ str(size) + 
	'-inch pizza with the following toppings: ')
	for topping in toppings:
		print('- ' + topping)
'''
make_pizza(16, 'pepperoni')
make_pizza(12,'mushrooms','green peppers','extra cheese')
'''
'''
def build_profile(first, last, **user_info):
	profile = {}
	profile['first_name'] = first
	profile['last_name'] = last
	for key, value in user_info.items():
		profile[key] = value
	return profile
	
user_profile = build_profile('albert','einstein',
                           location = 'princeton',
                           field = 'physics',
                           contribution = 'great',
                           )
print(user_profile)                          
'''
