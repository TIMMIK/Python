names = []
n = 1
while  True:
  ques = f"{n} - tag your friend : "
  name = input(ques)
  names.append(name)
  repeatly = input("Do you add name ? (YES / NO)")
  n += 1
  if repeatly != 'YES' :
    break
for name in names :
  print(f"{name} - is your bestie ")
