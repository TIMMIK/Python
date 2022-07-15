# practice-1
def avto_info(kompaniya, model, rangi, korobka, yili, narhi = None) :
  avto = {'kompaniya':kompaniya,
          'model':model,
          'rang':rangi,
          'korobka':korobka,
          'yil':yili,
          'narh':narhi}
  return avto

# practice-2
def avto_kirit():
  print("Saytimizdagi avtolar ro'yxatini shakllantiramiz")
  avtolar = []
  while True:
    print("\nQuydagi ma'lumotlarni kiriting", end = '')
    kompaniya = input("Ishlab chiqaruvchi : ")
    model = input("Modelni : ")
    rangi = input("Rang : ")
    korobka = input("Korobka : ")
    yili = input("Ishlab chiqarilgan yili : ")
    narhi = input("Narhi : ")
    avtolar.append(avto_info(kompaniya, model, rangi, korobka, yili, narhi))
    javob = input("Yana avto qo'shasizmi? (yes/no) : ")
    if javob == 'no':
      break
  return avtolar

# practice-3
def info_print(avto_info):
  """Avtomobillar haqida ma'lumotlar saqlangan lug'atini konsolga chiqaruvchi funksiya """
  print(f"{avto_info['rang'].title()} {avto_info['kompaniya'].upper()}"
       f"{avto_info['model'].upper()}, {avto_info['korobka']} korobka, "
       f"{avto_info['yil']}-yil, {avto_info['narh']}$")