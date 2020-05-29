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

# guessing game1
# guess = ""
# answer = "cheater"
# while guess != answer:
#   guess = input('guess the answer! : ') 

# print('guessed correctly')

# # guessing game2
# answer = "cheater"
# guess = input("guess the answer: ")
# guessCount = 0

# while guess != answer and guessCount < 3:
#   guess = input("keep guessing: ")
#   guessCount += 1

# if guessCount == 3:
#   print("you're out of guesses!")
# else: 
#   print("you guessed correctly!")

# rdm = ['df', 'dfs', 'sdfsdf', 'asf']
# rdmlength = len(rdm)

# for r in range(rdmlength):
#   print (rdm[r])

# power function1
# def powerfunc(a,b):
#   return a**b
# print(powerfunc(2,2))

# power function2

def powerfunc(a, b):
  anum = 1
  for bnum in range(b):
    anum = anum * a
  return anum

print(powerfunc(7,3))