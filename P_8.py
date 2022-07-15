# Ц Ы К Л Ы - for 
people = ['Tima', 'Doston', 'Shox', 'Shahob']
for class_name in people:
  print('It\'s', class_name)
  print('It\'s not', class_name)

num = [15,16,17]
for name_class in num:
  print(f"I'm {name_class} years old")

# квадрат чисел
a = list(range(10))
b = []
for name in a:
  b.append(name**2)
print(a)
print(b)

friends = []
print('mark your 5 besties')
for n in range(5):
  friends.append(input(f"{n+1}-mark your next frined :"))  
print(friends)