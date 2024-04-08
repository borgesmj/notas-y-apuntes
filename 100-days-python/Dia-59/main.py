def checkWord(word):
  check_word = word.strip().lower().replace(" ", "")
  for i in range (len(check_word)):
    if check_word[i] != check_word[len(check_word) - i - 1]:
      return f"{word.upper()} no es un palindromo"
    else:
      return f"{word.upper()} si es un palindromo"


word = input('introduzca su palabra:\n> ')
print(checkWord(word))
exit()

# Usando recursion

# def palindrome(word):
#   if len(word)<=1:
#     return True
#   if word[0] != word[-1]:
#     return False
#   return palindrome(word[1:-1])

# print(palindrome("racecar"))