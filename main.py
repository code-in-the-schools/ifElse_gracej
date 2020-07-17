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
word = input(str("word: "))

vowel = 1
consonant = 1

for x in list1:
  if (x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u' or x == 'A' or x == 'E' or x == 'I' or x == 'O' or x == 'U'):
    print (vowel * x)
  else:
    print (consonant * x)