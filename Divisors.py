# https://www.practicepython.org/exercise/2014/02/26/04-divisors.html

number = int(input("enter number: "))
divisor= list()
for i in range(1,number+1):
    if number%i == 0:
        divisor.append(i)
    i+=1
print(divisor)
