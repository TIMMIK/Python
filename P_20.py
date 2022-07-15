# Если количество аргументов неизвестно, добавьте * - это називается "args" --> arguments
print(' 1) way ' )
def summa(*sonlar): # sonlar - o'zgaruvchan argument
  """ KIRITILGAN SONLAR YOG'INDISINI HISOBLAYDIGAN FINKSIYA """
  yigindi = 0
  for son in sonlar :
    yigindi += son
  return yigindi
print(summa(1,2)) # 1+2=3
print(summa(1,2,3,4,5)) #1+2+3+4+5=15
print(summa(4,5,6,7)) # 4+5+6+7=22

print(' 2) way ' )

def summa(*sonlar):
  """ KIRITILGAN SONLAR YOG'INDISINI HISOBLAYDIGAN FINKSIYA """
  return sum(sonlar)
print(summa(1,2)) # 1+2=3
print(summa(1,2,3,4,5)) #1+2+3+4+5=15
print(summa(4,5,6,7)) # 4+5+6+7=22

# Добавьте две звездочки: ** перед именем параметра в определении функции - это називается "kwards" --> keywords
# Таким образом, функция получит словарь аргументов и сможет соответственно получить доступ к элементам
def info(kompany,model,**information):
  """ Avto haqidagi ma'lumotlarni lug'at ko'rinishida qaytaruvchi funksiya """
  information['kompany'] = kompany
  information['model'] = model
  return information

info1 = info("GM", "Malibu", color = 'black', year = 2019)
print(info1)
info2 = info("KIA", "K5", color = 'red', year = 2020)
print(info2)

