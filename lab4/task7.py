char = input("enter a letter: ")
vowel = ['a', 'e', 'i', 'o', 'u']

if len(char) > 1:
  print("character too long")
elif char.lower() in vowel:
  print("vowel")
else:
  print("consonant")