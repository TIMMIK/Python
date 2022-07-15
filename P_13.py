# method - .item()
phone = {
  'Me': 'iPhone-14 :',
  'Shox': 'iPhone-13',
  'Shaxzod': 'iPhone-12',
}
print(phone.items()) # items - это метод, выводит данные которые находятся в data type list(array) and in data type set(object)

for name, info in phone.items() :
  print(f'1 : {name} \n')
  print(f'2: {info} \n')

# method - keys()
cars = {
  "a":'supra', 
  "b":'dodge',
  "c":'mustang'
} 

for motor in cars.values() : # values - это метод, выводит данные которые находятся в data type list(array) and in data type set(object)
  print(motor)


for abc in cars.keys() : # keys - это метод, перевод --> "ключи", выводит имя данного 
  print(abc.capitalize())

brends = {
  'a':'SUPRA', 
  'b':'SUPRA', 
  'c':'MUSTANG', 
  'd':'MUSTANG', 
  'e':'BUGGATI', 
  'f':'BUGGATI'
}
sss = {
  'First', 'Second', 'Third'
}
print(type(sss)) # data type set, выводит дублированные значения не повторяя их, то есть не дублируя 
 
for anyClassname in set(brends.values()) : # SET - это метод, неупорядоченый, неизменяемый и не допускают дублированных значений
  print(anyClassname)
