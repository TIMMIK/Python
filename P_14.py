car0 = {
  'model':'supra',
  'color':'pink',
  'year' :2005,
  'cost' :'1500$',
  'km' : 100
}
car1 = {
  'model':'BMW',
  'color':'gold',
  'year' :2005,
  'cost' :'1000$',
  'km' : 300
}

cars = car0,car1
for car in cars :
  print(f"{car['model']},"
        f"{car['color']},"
        f"{car['cost']},")

tesla = [] 

for n in range(10):
  car2 = {
  'model':'nissan',
  'color':'grey',
  'year' :2006,
  'cost' :'2000$',
  'km' : 200
  }

tesla.append(car2)

for nissan in tesla[:2]:
  nissan['color']='red'
for nissan in tesla[:2]:
  print(nissan)
