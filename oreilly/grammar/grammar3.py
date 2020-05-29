# "editor.tokenColorCustomizations": {
#     "comments": "#12CBC4",
#     "textMateRules": [
#       {
#         "scope": "string.quoted.docstring.multi.python",
#         "settings": {
#           "foreground": "#f1dd83"
#         }
#       }
#     ]
#   }

# """
# write a meaningful docstring
# """
# """
# autoDocstring
# """

# guessing game 1
guess = ""
answer = "cheater"
while guess != answer:
  guess = input('guess the answer! : ') 

print('guessed correctly')

# # guessing game 2
answer = "cheater"
guess = input("guess the answer: ")
guessCount = 0

while guess != answer and guessCount < 3:
  guess = input("keep guessing: ")
  guessCount += 1

if guessCount == 3:
  print("you're out of guesses!")
else: 
  print("you guessed correctly!")

rdm = ['df', 'dfs', 'sdfsdf', 'asf']
rdmlength = len(rdm)

for r in range(rdmlength):
  print (rdm[r])

# power function 1
def powerfunc(a,b):
  return a**b
print(powerfunc(2,2))

# power function 2
def powerfunc(a, b):
  anum = 1
  for bnum in range(b):
    anum = anum * a
  return anum
print(powerfunc(7,3))

# grid list
gridlike = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]

for row in gridlike:
  for col in row:
    print(col)

for row in gridlike:
  print(row[1]

# translator for vowels are v 1
def translator(phrase):
  translation = ''
  for letter in phrase:
    if letter in "AEIOU":
      translation = translation + "V"
    elif letter in "aeiou":
      translation  = translation + "v"
    else:
      translation = translation + letter
  return translation
print(translator(input('insert what you want to translate: ')))

# translator for vowels are v 2
def translator(phrase):
  phrasel = list(phrase)
  for index in range(len(phrase)):
    if phrasel[index] in "AEIOU":
      phrasel[index] = 'V'
    elif phrasel[index] in "aeiou":
      phrasel[index] = 'v'
    else:
      continue
  return phrasel

print(('').join(translator(input("insert phrase to translate: "))))
