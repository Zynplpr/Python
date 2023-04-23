# https://www.practicepython.org/exercise/2014/03/12/06-string-lists.html

word = input("write a word: ")
if word == word[::-1]:
    print(f"{word} is a palindrome.")
else:
    print(f"{word} is not a palindrome.")
