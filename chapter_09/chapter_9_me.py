"""python crash course chapter 9"""


# classes
class Dog:
    """ a simple atempt to model a dog"""

    def __init__(self, name, age):
        """initialise name and age atributes"""
        self.name = name
        self.age = age

    def sit(self):
        """simulate a dog sitting in response to a comand"""
        print(f"{self.name} is now sitting")

    def roll_over(self):
        """simulate rolling over in response to a commmand"""
        print(f"{self.name} rolled over")

    def give_treat(self):
        print(f"{self.name} got a treat for being so good!")


my_dog = Dog("Toby", 10)

print(f"My dog's name is {my_dog.name}")
print(f"My dog is {my_dog.age} years old.")

my_dog.sit()

my_dog.roll_over()

jasmines_dog = Dog("Lokito", 3)
jasmines_dog.sit()
my_dog.sit()

my_dog.give_treat()
jasmines_dog.give_treat()


class Car:
    """ a simple attempt to represent a car """

    def __init__(self, make, model, year):
        """ initialise atributes to describe a car """
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """ return a neatly fortmatted descriptive name """
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """ print a statement showing the car's milage """
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """ set the odometer reading to the given value
        reject the change if it atempts to roll the odometer back """
        if mileage < self.odometer_reading:
            print("You're cheating")
        else:
            self.odometer_reading = mileage

    def increment_odometer(self, miles):
        """ add the given ammount to the odometer reading """
        self.odometer_reading += miles


my_new_car = Car("Honda", "Accord", "2007")

print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

my_new_car.odometer_reading = 200000
my_new_car.read_odometer()

my_new_car.update_odometer(40)
my_new_car.read_odometer()

my_new_car.update_odometer(4)
my_new_car.read_odometer()

my_new_car.increment_odometer(20)
my_new_car.read_odometer()


class Battery:
    """ a simple atempt to model a battery for an electric car """

    def __init__(self, battery_size=75):
        """ initialize the battery's attributes """
        self.battery_size = battery_size

    def describe_battery(self):
        """ print a statement describing the battery size """
        print(f"This car has a {self.battery_size} kw battery.")

    def get_range(self):
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go {range} miles on a full charge.")


# inheritance

class ElectricCar(Car):
    """ represent aspects of a car specific to electric veichles """

    def __init__(self, make, model, year):
        """ initialise atributes of the parent class """
        super().__init__(make, model, year)
        self.battery = Battery()

    def fill_gas_tank(self):
        """ electric cars don't have gas tanks """
        print("This car doesn't need a gas tank.")


my_tesla = ElectricCar("Tesla", "s", "2019")
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.fill_gas_tank()
my_tesla.battery.get_range()

# imagine i saved the above classes in a file called car.py
# from car import Car
# from car import ElectricCar
# from car import Car, ElectricCar
# import car  # if I did this, I would have to call the classes like car.Car etc

# from Car import *
# from car import ElectricCar as EC

from random import randint

number = randint(1, 60)
print(number)

from random import choice

names = ["rosemary", "zari", "jasmine"]

first_up = choice(names)
print(first_up)
