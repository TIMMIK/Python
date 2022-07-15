class Talaba:
  def __init__(self,ism,familiya,tyil):
    self.ism = ism
    self.familiya = familiya
    self.tyil = tyil
    self.bosqich = 1
    
    
  def get_info(self):
    return f"{self.ism} {self.familiya}. {self.bosqich}-bosqich talabasi "
  
  def get_name(self):
    return self.ism

  def get_lastname(self): # показывает
    return self.familiya

  def set_bosqich(self,yangi_bosqich): # изменяет
    self.bosqich = yangi_bosqich

  def update_bosqich(self): # добавляет 
    self.bosqich += 1


talaba1 = Talaba('Timur','Tursunov',2005)

print(talaba1.get_info())
print(talaba1.get_name())
print(talaba1.get_lastname())

# Функция dict() создает словарь.
# Словарь — это неупорядоченная, изменяемая и индексируемая коллекция.
print(talaba1.__dict__)

print(talaba1.update_bosqich())
print(talaba1.get_info())

# Функция dir() возвращает все свойства и методы указанного объекта без значений.
# Эта функция вернет все свойства и методы, даже встроенные свойства, которые используются по умолчанию для всех объектов.
def see_methods(klass):
  return [method for method in  dir(klass) if method.startswith("__")]
print(see_methods(Talaba))