# В Python вы используете ключевое слово import, чтобы сделать код в одном модуле доступным в другом. Импорт в Python важен для эффективного структурирования кода. Правильное использование импорта сделает вас более продуктивным, позволяя повторно использовать код, сохраняя при этом ваши проекты.

print('1) way')
from calendar import c
import for_P_21 # for_P_21. - другой файл 
className = for_P_21.avto_info("GM ", "Malibu", "blvck", "avtomatic", 2020, 40000) # info2 - данная находящаяся в файле for_P_21
for_P_21.info_print(className) # info2_print - название функции, то есть def, info_print - это можно сказать имя или название def - это функция

print('2) way')
# Нужно создать псевдоним при импорте модуля, используя ключевое слово as
import for_P_21 as anyName
className = for_P_21.avto_info("GM ", "Malibu", "blvck", "avtomatic", 2020, 40000) 
anyName.info_print(className)

print('3) way')
# импорт из модуля - from ... import ...
# можно импортировать только части из модуля, используя ключевое слово from
from for_P_21 import avto_info, info_print
className = avto_info("GM ", "Malibu", "blvck", "avtomatic", 2020, 40000) 
info_print(className)

print('4) way')
from for_P_21 import avto_info as ainfo, info_print as iprint
className = ainfo("GM ", "Malibu", "blvck", "avtomatic", 2020, 40000) 
iprint(className)

# module - math
import math
x = 400
print(math.sqrt(x)) # Метод math.sqrt() возвращает квадратный корень числа
print(math.pow(5,3)) # 5 в кубе
print(math.pow(5,2)) # 5 в квадрате
print(math.pi) # показывает чему равно число π
print(math.log(x)) # вычисляет логарифм числа, логарифм - это числа x по основанию а это показатель степени, в которую нужно возвести а, чтобы получить x

# randint() - method
import random as name
otherName = name.randint(10,50) # random intiger - показывает рандомное целое число
print(otherName)

# choice - method
cars = [ 'PORSHE', 'NISSAN', 'MUSTANG', 'MERCEDES', 'BUGGATI']
car = name.choice(cars) # выбирает рандомное данное
print(car)

# shuffle - method
x = list(range(11))
name.shuffle(x) # измениет порядок элементов в списке
print(x)