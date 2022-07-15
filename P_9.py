cars = [ 'PORSHE', 'NISSAN', 'MUSTANG', 'MERCEDES', 'BUGGATI']
# == - equal, знак равенства
# != - not equal знак неравенства
for mot in cars: 
  if mot == 'PORSHE':
    print(mot.upper())
  else:
    print(mot.title())

not_equal = [1,2,3,4,5]
for eye in not_equal :
  if eye != 5 :
    print(' NOT EQUAL ')
  else :
    print('EQUAL')

answer = float(input(' 2 x 2 = '))
if answer != 4:
  print('not it was 4')

age = int(input('your age - '))
if age >= 18 :
  print('come in')
else : 
  print('go away')

login = input('Enter login : ')
if len(login) <= 3 :
  print(' Welcome ')
else : 
  print(' Try again ')

# первое условие это для if, а второе это для else 
x , y = 5 , 10
print('x > y') if x > y else print('x < y')