# https://www.practicepython.org/exercise/2014/02/15/03-list-less-than-ten.html

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
newlist= list()
for element in a:
    if element<10:
        newlist.append(element)
        print(newlist)
print(newlist)
