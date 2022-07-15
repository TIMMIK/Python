alpha = ['_B M W_', 'MERCEDES', 'SUPRA', 'NISSAN', 'PORSHE', 'AUDI']
alpha.sort() # сортирует слова в алфавитном порадке
print(alpha)

betta = ['_b m w_', 'MERCEDES', 'SUPRA', 'NISSAN', 'PORSHE', 'audi']
betta.sort() # сортирует даже по размеру буквы, если буква большая, то sort начинает сортировать с большого
print(betta)

gamma = ['BUGGATI', 'MERCEDES', 'SUPRA', 'NISSAN', 'PORSHE', 'MUSTANG']
gamma.sort(reverse=True) # сортирует с конца до начала. то есть сортирует наоборот
print(gamma)

lucky = ['BUGGATI', 'MERCEDES', 'SUPRA', 'NISSAN', 'PORSHE', 'MUSTANG']
print(sorted(lucky)) # сортированный, то есть className сортируется не изменяя свою данную
print(sorted(lucky,reverse=True)) # сортированный, то есть className сортируется с конца до начала не изменяя свою данную

n =[1,2,3,4,5,6,7,8,9] # for numbers
n.sort()
n.sort(reverse=True)
print(n)

num = [1,2,3,4,5,6,7,8,9] # for numbers
print(sorted(num))
print(sorted(num,reverse=True))

res = ['SUPRA', 'PORSHE', 'NISSAN', 'MUSTANG', 'MERCEDES', 'BUGGATI']
res.reverse() #  не сортиуя выводит данные с конца до начала
print(res)

leen = ['SUPRA', 'PORSHE', 'NISSAN', 'MUSTANG', 'MERCEDES', 'BUGGATI']
print(len(leen)) # len - показывает сколько данных есть в листе типа данных

ran = [0,1,2,3,4,5,6,7,8,9,10]
# list - для добавление данного в лист [] - array
ran = list(range(-1,11)) # range - создает или показывает данные от начала до конца (от А до Я)
# range без list не работает
print(ran)

# добавление чисел по 2 раза. то есть (2,4,6,8,10)
# 1-ое число это начало, 2-ое это конец, а третье это указывает по сколько раз нужно добавить число или данный
one = list(range(0,10,2)) # тут по два раза добавляет
print(one)

xxx = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
mmm = max(xxx) # показывает самую большую цифру или данную  
print(mmm) # ответ : 20

nnn = [10,11,12,13,14,15,16,17,18,19,20]
iii = min(nnn) # показывает самую маленькую цифру или данную  
print(iii) # ответ : 10

siu = [5,10,15,20,25,30,35]
pls = sum(siu) # сумирует все числа или данные находящиеся внутри листа [] - array
print(pls)

motors = ['SUPRA', 'PORSHE', 'NISSAN', 'MUSTANG', 'MERCEDES', 'BUGGATI']
print(motors[2:6]) # показывает данные от 2 до 6

class_name = motors[:] # чтобы копировать данные на другой class_name
print(class_name)

# если лист открыт простой скобкой то это const ,а если лист открыт квадратной скобкой то это let
tup = ('SUPRA', 'PORSHE', 'NISSAN', 'MUSTANG', 'MERCEDES', 'BUGGATI')
tup = tuple(tup) # стал const
print(tup)

