#  while - это цикл
num = 1
while num <= 5 :
  print(num, end = "")
  num += 1 # num = num + 1
print('NUM IS ENDED')
#  1) way
question = 'Type anything'
question += " or type 'exit' for stop process : "
val = ''
while val != 'exit' :
  val = input(question)
  if val != 'exit':
    print(float(val)**2)
# break - для останавливания кода или функции
#  2) way
while True : # для бесконечного цикла, надо добавить код --> True
  val = input(question)
  if val == 'exit' :
    break
  else:
    print(float(val)**2)
print('SIKL WHILE IS ENDED')

nums = list(range(1,11))
for n in nums :
  if n == 5 :
    continue # Ключевое слово continue используется для завершения текущей итерации в цикле for (или в цикле while) и продолжается до следующей итерации.
  print(f"{n} ning kvadrati {n**2} ga teng")
