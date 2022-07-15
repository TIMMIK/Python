# key words
car_0 = {"a":'supra', "b":'dodge'}
print(car_0["a"])
print( car_0["b"])

# vocab
en_uz = {'apple':1000, 'banana':9.90}
print(en_uz['apple'])
print( en_uz['banana'])
del en_uz['banana'] # for deleting info in list

phone = {
  'Me': 'iPhone-14 :',
  'Shox': 'iPhone-13',
  'Shaxzod': 'iPhone-12',
}
# get() - это метод, для выбора или для вывода элемента в листе 
newClass_name = phone.get("Me", "Shox") # выодит информацию внутри даннаго 'Me'
oldClass_name = en_uz.get('apple') 
print(newClass_name,oldClass_name) 