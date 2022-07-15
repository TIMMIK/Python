# f-string
a = "SOMETHING"
b = "ELSE"
c = f"{a} {b}"
print(f"{a} NEW {b}"), print(c)

# \t - сотавляет от себя длинный пробел
print('\t\tT I M U R')
# Python metod()
up = "upper case"
print(up.upper())  # сделает текст большим

low = "LOWER CASE"
print(low.lower()) # сделает текст маленьким

tite = 'It\'s title' 
print(tite.title()) # показывает каждое слово с большой буквойб которое находится в тексте 

cap = "CAPITALIZE " 
print(cap.capitalize()) # делает заглавной первую букву слова

fruit = "   apple"
print('It\'s ' + fruit.lstrip()) # удаляет пустое место в левом части слова

car = "SUPRA   "
print(car.rstrip() + " is best") # удаляет пустое место в правом части слова

boat = "     warship     "
print(boat.strip()) # удаляет пустое место в обе части слова

inp = input(" type here ") # тут можно написать после слова " here "
print(inp) # помогает написать в результате