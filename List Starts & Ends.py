# https://www.practicepython.org/exercise/2014/04/25/12-list-ends.html

a = [5, 10, 15, 20, 25]
b = [5,4,2,6,9,5,2,2,4,6,134865]
def take_number(list):
    return [list[0], list[-1]]
newfirstlist = take_number(a)
print(newfirstlist)
newsecondlist = take_number(b)
print(newsecondlist)
