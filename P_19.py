def bahola(ismlar) :
  baholar = {}
  while ismlar :
    ism = ismlar.pop()
    baho = input(f"Talaba {ism.title()}ning bahosini kiriting : ")
    baholar[ism]=int(baho)
  return baholar
talabalar = ['ali', 'hasan', 'timur']
baholar = bahola(talabalar[:])
print(baholar)