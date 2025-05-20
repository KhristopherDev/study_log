from abc import ABC, abstractmethod

class Car(ABC):
  def __init__(self, brand):
    self.__brand = brand
  
  def get_brand(self): return self.__brand
  def set_brand(self, brand): self.__brand = brand

  @abstractmethod
  def speak(self): pass

class Fiat(Car):
  def speak(self): return f"Este carro é da marca {self.get_brand()}."

class Ford(Car):
  def speak(self): return f"Este carro é da marca {self.get_brand()}."

class Porche(Car):
  def speak(self): return f"Este carro é da marca {self.get_brand()}."

cars = [Fiat("Fiat"), Ford("Ford"), Porche("Porche")]

for a in cars:
  print(a.speak())