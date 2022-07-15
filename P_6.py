# className = [ ..., ..., ...] - data type list
a = ["shokh", "tima", "aziz", "javokh"]
a[-1] = "elnur" # [-1] - добавляет данную к концу листа типа данных
print(a)

b = [10, 20, 30, 40]
print(b[3])
print(b[0] + b[1] )

c = ["shokh", "tima", 10, 20]
print(c[1])

d = []
print(d) 

# .append() - добавляет данную к концу листа типа данных
e = ["shokh", "javokh", "aziz", "tima"]
e.append("doston")
print(e)

# insert - добавляет данную в любое место листа типа данных
# индекс - это расположение данного
r = [ "javokh", "aziz","shokh", "tima"]
r.insert(0,"javlon") # 0 - это индекс, а "javlon" это данная которую мы добавили 
r.insert(3,"mirjahon") # 3 - это индекс, а "mirjahon" это данная которую мы добавили
print(r)

# del
cars = []
cars.append("supra")
cars.append("dodge") # we are deleted "dodge"
cars.append("nissan")
cars.append("merc")
cars.append("mustang")
# del --> delete - помогает удалить данную внутри листа типа данных 
del cars[1] # or
# remove - помогает удалить данную внутри листа типа данных
cars.remove("merc") # тут мы указываем данную
print(cars)

# pop() - отбирает элемент от листа типа данных, на отдельный другой className
ourClass = ["aziz", "shohjahon", "timur"]
otherClass = ourClass.pop(0) # 0 - это индекс и вывели aziz на otherClass
print(ourClass) # остались ["shohjahon", "timur"]
print(otherClass) # вышло aziz

# замена или добавление  данного 
school = ["desk", "basketball", "else"]
school[0] = school[0] + "top"
school[1] = "something " + school[2]
print(school)