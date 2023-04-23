# https://www.practicepython.org/exercise/2014/04/30/13-fibonacci.html

def fibonacci():
    count = int(input("How many Fibonacci number do you want? "))
    i = 1
    if count == 0:
        fibon = []
    elif count == 1:
        fibon = [1]
    elif count == 2:
        fibon = [1,1]
    elif count > 2:
        fibon = [1,1]
        while i < (count - 1):
            fibon.append(fibon[i] + fibon[i-1])
            i += 1

    return fibon
