'''
class Dog():
	def __init__(self, name, age):
	    self.name = name
	    self.age = age
	
	def sit(self):
		print(self.name.title() + " is now sitting.")
		
	def roll(self):
		print(self.name.title() + " rolled over!")

my_dog = Dog('william', 6)


print("My dog's name is " + my_dog.name.title() +'.')

print("My dog is " + str(my_dog.age) + " years old.")

my_dog.sit()
my_dog.roll()
'''


class Car():
	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0
		
	def get_descriptive_name(self):
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name.title()
		
	def updata_odometer(self,mileage):
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You can't roll back an odometer!")
	def read_odometer(self):
		print("This car has " + str(self.odometer_reading) + " miles on it.")

	def increment_odometer(self, miles):
		self.odometer_reading += miles	
my_car = Car('audi','a4',2016)
print("I have a " + my_car.get_descriptive_name())
my_car.updata_odometer(23)
my_car.read_odometer()		

my_used_car = Car('subaru', 'outback',2013)
print(my_used_car.get_descriptive_name())

my_used_car.updata_odometer(23500)
my_used_car.read_odometer()
	
my_used_car.increment_odometer(100)
my_used_car.read_odometer()

class Battery():
	def __init__(self, battery_size = 70):
		self.battery_size = battery_size
	def describe_battery(self):
		print("This car has a" + str(self.battery_size) + '-kwh battery.')
	def get_range(self):
		if self.battery_size == 70:
			range = 240
		elif self.battery_size == 85:
			range = 270
		message = 'This car can go approximately ' + str(range) + ' miles on a full charge.'
		print(message)

class ElectricCar(Car):
	def __init__(self,make,model,year):
		super().__init__(make,model,year)
		self.battery = Battery()
	def fill_gas_tank():
		print("This car doesn't need a gas tank!")
my_tesla = ElectricCar('tesla','moeld s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
