# https://www.practicepython.org/exercise/2014/03/19/07-list-comprehensions.html

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
even = list()
for number in a:
    if number%2 ==0:
        even.append(number)
print(even)
