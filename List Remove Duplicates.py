# https://www.practicepython.org/exercise/2014/05/15/14-list-remove-duplicates.html

a = [2,3,7,3,2,6,8,3,5,234,46,765,2,34,89,567,234,63,45,653,34,23,556,234]
def duplist(list_name):
    new_list = list()
    for number in list_name:
        if number not in new_list:
            new_list.append(number)
    return new_list

def main():
    b = duplist(a)
    print(b)

if __name__ == "__main__":
    main()

# or

a = [2,3,7,3,2,6,8,3,5,234,46,765,2,34,89,567,234,63,45,653,34,23,556,234]
numbers = set()

for number in a:
    numbers.add(number)
print(numbers)


