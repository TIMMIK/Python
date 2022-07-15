def createName(name,surname) :
  fullName = f"{name},{surname}"
  # Ключевое слово return предназначено для выхода из функции и возврата значения.
  return fullName # повторяет инфо который находится в данном
anyClass_name =  createName('TIMUR', 'TURSUNOV')
print(anyClass_name)

def cars(year,color,model = '') :
  if model: # removed model in IF function
    className = f"{year},{color},{model}"
  else:
    className = f"{year},{model}"
  return className
anyClass1 = cars(2005, 'S U P R A')
anyClass2 = cars(2010,' pink','N I S S A N')
print( f'I prefer {anyClass1} than {anyClass2} ')

def oraliq(min,max):
  numbers = []
  while min < max :
    numbers.append(min)
    min += 1
  return numbers
print(oraliq(0,10))
print(oraliq(10,21))