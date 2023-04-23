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

# There is this case where we don't have the exact list but we ask Python to randomly create one and then the same... + common list is sorted.

import random
a = random.sample(range(1,101),10)
b = random.sample(range(1,101),17)
common = list()
for number in a:
    if number in b:
        if number in common:
            pass
        else:
            common.append(number)
            common.sort()
            print(ortak)
