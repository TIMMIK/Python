# создание класса в Питоне
class ClassName:
# функция __init__() нужна для присвоения значений свойствам объекта или других операций, которые необходимо выполнить при создании объекта
  def __init__(self,ism,familiya,tyil):
    self.ism = ism
    self.familiya = familiya
    self.tyil = tyil
    
  def anyName(self):
    return f"Ismim {self.ism} {self.familiya}, {self.tyil} da tug'ilganman"

first = ClassName('Timur','Tursunov',2005)