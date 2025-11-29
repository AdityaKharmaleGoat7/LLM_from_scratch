
import numpy as np
import pandas as pd

# import torch

print("This script will be used to maintain my side projects")

print()


class Myclass:
 x = 5

# __init__ is created automatically during the creation of class
class Person:
 def __init__(self, name, age):
  self.name = name
  self.age = age 

 def __str__(self):
  return f"{self.name}({self.age})"

 def myFunc(self):
  print("Hello my name is -", self.name)

class derived(Person):
 def __init__(self, name, age, year):
  super().__init__(name, age)
  self.year = year

p1 = Person("Adidon", 22)

p2 = derived("vivek", 24, 2019)

print("Hi, I'm", p2.name, "I'm", p2.age, "years old, and I graduated in", p2.year)
 
