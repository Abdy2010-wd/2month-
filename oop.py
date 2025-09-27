#Задание 1



# class Persоn:
#     def __init__(self):
#         self.__age = None
#
# def set_age(self, age):
#     if age < 0:
#         raise ValueError("Возраст не может быть отрицательным!")
#     self.__age = age
#
# def get_age(self):
#     return self.__age
# p = Persоn()
# p.set_age()
# print(set_age())
# #2
#
# class Animаl:
#     def __init__(self, name):
#         self.name = name
#
# def speak(self):
#     return "I am an animal"
#
#
# class Dog(Animаl):
#     def speak(self):
#         return "Woof"
#
# class Сat(Animаl): # обратите внимание, что в слове "Cat" стоит похожая буква "С"
#     def speak(self):
#         return "Meow"
# dog = Dog("Buddy")
# cat = Сat("Kitty")
# print(dog.name, dog.speak())
# print(cat.name, cat.speak())
# #3
# class Vehiclе:
#     def move(self):
#         return "Vehicle is moving"
#
# class Car(Vehiclе):
#     def move(self):
#         return "Car is driving"
#
# class Bicyclе(Vehiclе):
#     def move(self):
#         return "Bicycle is pedaling"
#
# def move(vehicle: Vehiclе):
#     return vehicle.move()
# car = Car()
# bike = Bicyclе()
# print(move(car))
# print(move(bike))

#4
from abc import ABC, abstractmethod
import math

class Shape(ABC): # наследуемся от ABC
@abstractmethod

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

def area(self):
    return self.width * self.height


class Circle(Shape):

def __init__(self, radius):
    self.radius = radius

def area(self):
    return math.pi * (self.radius ** 2)


rect = Rectangle(10, 5)
circle = Circle(7)

print(rect.area())
print(circle.area())
