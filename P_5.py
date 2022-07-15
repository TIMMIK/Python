# type - это атрибута, помогает узнать тип данных

# int --> integer - это целые числа
a = 20 
print(type(a))
# float -  это нецелые числа
b = 5.5
print(type(b))
# how write million
million = 1_500_000
print(million)
# some variables in one line
# x,y,z --> let - изменяемый, то есть маленькие буквы это let
# X,Y,Z --> const - неизменяемый, то есть большие буквы это const
x = 16
y = "My age : "
print(y + str(x))# str() - выводит любую тип данных в string тип данных

# МЕЖДУ NUMBERом и STRINGом нельзя поставить математические выражени
print(str(400)) # str() - переводит на текстовой тип данных
print(int(10.5)) # int() - переводит на целое число
print(float(10)) # float() - переводит на нецелое число
# EXAMPLE
o = int(input("your year - "))
u = 2020 - o
print(u," , and you are clever")