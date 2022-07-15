class Avto:
  __num_avto = 0
  def __init__(self,make,model,yil):
    self.make = make
    self.model = model
    self.yil = yil
    Avto.__num_avto += 1
  # 1) way
  def __str__(self):
    return f"Avto: {self.make} {self.model}"
  # 2) way - is better than 1) way
  # Возвращает читаемую версию объекта
  def __repr__(self):
    return f"Avto: {self.make} {self.model}"
  
  def __eq__(self, y): # равно или неравно
    return self.yil == y.yil
    
  def __lt__(self, y): # больше или меньше
    return self.yil < y.yil
  
  def __le__(self, y): # больше или меньше либо равно
    return self.yil < y.yil

class AvtoSalon:
  def __init__(self,name):
    self.name = name
    self.avtolar = []

  def __repr__(self):
    return f'{self.name} avtosaloni'
  
  def __getitem__(self,index):
    return self.avtolar[index]

  def __setitem__(self,index,qiymat):
    return self.avtolar[index] == qiymat

  def __call__(self,*qiymat):
    if qiymat:
      for avto in qiymat:
        self.add_avto(avto)
    else:
      return [avto for avto in self.avtolar]
  
  def __add__(self,boshqa_salon):
    if isinstance(boshqa_salon,AvtoSalon):
      yangi_salon = AvtoSalon(f"{self.name} {boshqa_salon.name}")
      yangi_salon.avtolar = self.avtolar + boshqa_salon.avtolar
      return yangi_salon

  def add_avto(self,*qiymat):
    for avto in qiymat:
      # Функция isinstance() возвращает True, если указанный объект имеет указанный тип, иначе False.
      if isinstance(avto,Avto):
        self.avtolar.append(avto)
      else:
        print('Avto kiriting')

salon1 = AvtoSalon("MaxAvto")
print(salon1[:])
print(salon1.name)
avto1 = Avto("GM", "Malibu", 2020)
print(salon1(avto1))
avto2 = Avto("GM", "Cobalt", 2015)
print(avto1 == avto2)  
print(avto1 != avto2) 
print(avto1 > avto2) 
print(avto1 < avto2)
print(avto1 <= avto2) 
print(avto1 >= avto2) 
print(repr(avto1))