# SHORT WAY
age = int(input('How old are you ? '))
if age <= 5 : 
  val = "Free "
elif age <= 12 :
  val = 4000
elif age <= 16 :
  val = 8000
else : 
  val = 12000  
print(f"For you {val}")

# or - или; работает, тогда когда хотя-бы правильна одна функция или действие
day = input('Today is - ')
if day.lower() == 'sunday' or day.upper() == 'monday' or day.title() == 'friday' :
  print('You may rest')
else : 
  print('You must work')

# and - и; работает, тогда когда правильна две или более функции или действии
month = input('What is current month ?')
degree = int(input('what is today\'s degree ?'))
if month.lower() == 'october' and degree <= 27:
  print('You can walk')
elif month.lower() == 'april' and degree >= 27:
  print('You must stay at home')



overall = 10000
tea = True 
koktail = False
if tea and koktail :
  overall = overall + 2000
elif tea or koktail :
  overall = overall + 200
print(f"The {overall} for you")

# Тут рассмотрели все функции if по отдельности, и не оставляет ни один if
a = 100
b = True # 1
c = False # 0
d = True # 1

if b : 
  print('It\'s B')
  a = a + 200

if c :
  print('It\'s C')
  a = a + 300

if d :
  print('It\'s D')
  a = a + 400

# для проверки функции в data type string
menu = ['burger', 'osh', 'shashlik']
food = input(" What you prefer ?")
if food.lower() in menu : # in - в, проверяет данную которая есть в листе
  print('It\'s IN')
elif food.title() not in menu : # not in - не в, проверяет данную которая нет в листе
  print('It\'s NOT IN')
else :
  print('It\'s nothing')