import math
# # Ключевое слово lambda используется для создания небольших анонимных функций.
# # Лямбда-функция может принимать любое количество аргументов, но может иметь только одно выражение.
# # Выражение оценивается, и результат возвращается.
uzunlik = lambda pi, r : 2*pi*r
print(uzunlik(math.pi,10))

def daraja(n) :
  return lambda x : x**n

kvadrat = daraja(2)
kub = daraja(3)
print(f"3-ning kvadrati {kvadrat(5)} ga,"
      f"kubi {kub(4)} ga teng")

# # Функция map() выполняет указанную функцию для каждого элемента в итерируемом объекте.
# # Элемент отправляется функции в качестве параметра.
from math import sqrt
numbers = list(range(11)) 
ildizlar = list(map(sqrt,numbers)) # функция - map() действует на каждый данный, such as FOR
print(ildizlar) 

# # функция для вычесление квадратов записанных чисел :
raqamlar = list(range(11)) 
kvadratlar = list(map(lambda x:x*x, raqamlar))
print(kvadratlar)

# # Метод sample() возвращает список со случайным выбором указанного количества элементов из последовательности
import random as r
sonlar1 = r.sample(range(100),10) # выбирает 10 рандомные числа 
sonlar2 = r.sample(range(100),5) # выбирает 5 рандомные числа 
print(sonlar1,sonlar2)
def juftmi(x):
  """x juft bo'lsa True, aks holda False qaytaradi"""
  return x%5==0 


# # Функция filter() возвращает итератор, если элементы фильтруются с помощью функции, чтобы проверить, принят ли элемент или нет
# # Итерация - повторение какого-либо действия
juft_sonlar = list(filter(juftmi,sonlar1)) #  Функция filter() берет себе одну функцию(juftmi), и один лист(data type array in JS)
print(juft_sonlar)

people = ['Tima', 'Doston', 'Shox', 'Shahob']
harf1 = 'S' 
peoples = list(filter(lambda clas : clas.startswith(harf1),people))
harf2 = 'a'
peoples = list(filter(lambda clas : clas.endswith(harf2),people))
print(peoples)