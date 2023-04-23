# https://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html

try:
    num = input("Enter a number: ")
    number = int(num)
    if number%4 == 0:
        print(f"{number} is multiple of 4")
    elif number%2 == 0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")

except ValueError:
    print("enter number!!!")


