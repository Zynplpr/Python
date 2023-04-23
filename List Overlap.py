# https://www.practicepython.org/exercise/2014/03/05/05-list-overlap.html

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
common = list()
for number in a:
    if number in b:
        if number in common:
            pass
        else:
            common.append(number)
            print(common)
            
# or we can use sets to do this since sets don't contain duplicates.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
s = set()
for number in a:
    if number in b:
        s.add(number)
    else:
        pass
print(s)
