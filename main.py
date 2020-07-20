#ask the user their name
name = input(str("what is your name? "))

#convert into lowercase
print(name.lower())


###

#input a word
word = input(str("word: "))

#convert the word to a list
list1 = list(word)

#find if a vowel or consonant
for i in list1:
  if (i == "a" or i == "e" or i == "i" or i == "o" or i == "u" or i == "A" or i == "E" or i == "I" or i == "O" or i == "U"):
    print(i, ":", "vowel")
  else:
    print(i, ":", "consonant")
  


###

vowel = 0
consonant = 0

for x in list1:
  if (x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u' or x == 'A' or x == 'E' or x == 'I' or x == 'O' or x == 'U'):
    vowel = vowel + 1
  else:
    consonant = consonant +1
print("vowels:", vowel)
print("consonants:", consonant)

###

#input a word
word2 = input(str("word: "))

#convert the word to a list
list2 = list(word2)

#find if a vowel or consonant
for i in list2:
  if (i == "a" or i == "e" or i == "i" or i == "o" or i == "u" or i == "A" or i == "E" or i == "I" or i == "O" or i == "U"):
    print(i, ":", "vowel")
  elif (i != "a" or i != "e" or i != "i" or i != "o" or i != "u" or i != "A" or i != "E" or i != "I" or i != "O" or i != "U" or i != "!"):
    print(i, ":", "consonant")
  else:
    print(i, ":", "special character")