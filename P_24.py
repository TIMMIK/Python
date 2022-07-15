import random
from for_P_24_UZwords import words

def get_word():
  word = random.choice(words)
  while "-" in word or ' ' in word:
    word = random.choice(words)
  return word.upper()


def display(user_letters,word): # display - function, проверяет данную которое находится в переменной
  diplay_letter = ""
  for letter in word:
    if letter in user_letters.upper():
      diplay_letter += letter
    else:
      diplay_letter += "-"
  return diplay_letter

def play():
    word = get_word()
    word_letters = set(word)
    user_letters = ""
    print(f"Men {len(word)} honali so'z o'yladim. Topa olasizmi?")
    print(word)
    while word_letters:
        print(display(user_letters, word))
        if user_letters:
            print(f"Shu vaqtgacha topgan harflaringiz : {user_letters}")

        letter = input("Harf kiriting : ").upper()
        if letter in user_letters:
            print("Bu harfni avval kiritgansiz. Bosgqa harf kiriting :")
            continue
        elif letter in word:
            word_letters.remove(letter)
            print(f"{letter} Harfi to'g'ri")
        else:
            print("Bunday harf yo'q")
        user_letters += letter
    print(f"Tabriklayman! {word} so'zini {len(user_letters)} ta urinishda topdingiz")


play()