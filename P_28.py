# I N C A P S U L A T I O N
from uuid import uuid4 # uuid4 - it's function, for creating random ID numbers
class Avto:
  def __init__(self,make,model,km = 0):
    self.make = make
    self.model = model
    self.__km = km
    self.__id = uuid4()
  print(uuid4())

  def get_km(self):
    return self.__km


  def get_id(self):
    return self.__id # for creating const ID number
  
avto1 = Avto("GM", "Malibu", 10000)
print(avto1.get_km())
print(avto1.get_id())

class Me:
  my_age = 16
  def __init__(self, name, surname, birthYear = 2005):
    self.name = name
    self.surname = surname
    self.birthYear = birthYear
    Me.my_age += 1  

  @classmethod
  def get_my_age(cls):
    return cls.my_age
  
print(Me.get_my_age())
man = Me("Timur", "Tursunov")
print(man)

# from "FILE" import class1, class2 - создает возможность указывает на несколько классы
class class1:
  pass # проходить, то есть пропустит этот класс

class class2:
  pass # проходить, то есть пропустит этот класс
