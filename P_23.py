import random

def sontop(x = 10):
  tasodifiy_son = random.randint(1,x)
  print(f"Men 1 dan {x} gacha son o'yladim. Topishga harakat qiling? :")
  taxminlar = 0
  while True:
    taxminlar += 1
    taxmin = int(input("-->"))
    if taxmin < tasodifiy_son:
      print("Xato man o'ylagan son bundan kattaroq. Yana harakat qiling:")
    elif taxmin > tasodifiy_son:
      print("Xato man o'ylagan son bundan kichikroq. Yana harakat qiling:")
    else:
      break
  print(f"Siz {taxminlar} taxmin bilan topdingiz")
  return taxminlar
sontop()

def sontop_pc(x = 10): 
    input(f"1 dan {x} gacha son oylang va istalgan tugmani bosing. Men topaman ") 
    quyi = 1 
    yuqori = x 
    taxminlar = 0 
    while True: 
        taxminlar +=1 
        if quyi != yuqori: 
            taxmin = random.randint(quyi,yuqori) 
        else: 
            taxmin = quyi 
        javob = input(f'Siz {taxmin} sonini oyladingiz: togri (t),' 
                      f'men oylagan son bundan kataroq (+), yoki kichiroq (-)'.lower()) 
        if javob == "-": 
            yuqori = taxmin -1 
        elif javob == "+": 
            quyi = taxmin + 1 
        else: 
            break  
    print(f"Men ya'ni PC {taxminlar} ta urinishda topdim") 
 
sontop_pc() 
         