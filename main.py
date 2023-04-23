"""
# https://www.practicepython.org/exercise/2014/01/29/01-character-input.html
# Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.
# Add on to the previous program by asking the user for another number and printing out that many copies of the previous message.

name = input("What's your name?: ")
age = int(input("What's your age?: "))
repetition = int(input("how many times repeat?: "))
for i in range(1,repetition+1):
    print(f"{name} you will turn 100 years old in {100-age} years ",end="-")
"""
"""
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
"""
"""
num = int(input("enter num: "))
if num%2 == 0:
    if num%5 !=0:
        print(num)
    else:
        exit()

else:
    exit()
"""
"""
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
newlist= list()
for element in a:
    if element<10:
        newlist.append(element)
        print(newlist)
print(newlist)
"""
"""
number = int(input("enter number: "))
divisor= list()
for i in range(1,number+1):
    if number%i == 0:
        divisor.append(i)
    i+=1
print(divisor)
"""
"""
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
ortak = list()
for number in a:
    if number in b:
        if number in ortak:
            pass
        else:
            ortak.append(number)
            print(ortak)
"""
"""
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
s = set()
for number in a:
    if number in b:
        s.add(number)
    else:
        pass
print(s)
"""
"""
import random
a = random.sample(range(1,101),10)
b = random.sample(range(1,101),17)
ortak = list()
for number in a:
    if number in b:
        if number in ortak:
            pass
        else:
            ortak.append(number)
            ortak.sort()
            print(ortak)
"""
"""
word = input("write a word: ")
if word == word[::-1]:
    print(f"{word} is a palindrome.")
else:
    print(f"{word} is not a palindrome.")
"""
"""
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
even = list()
for number in a:
    if number%2 ==0:
        even.append(number)
print(even)
"""
"""
a = [5, 10, 15, 20, 25]
b = [5,4,2,6,9,5,2,2,4,6,134865]
def take_number(list):
    return [list[0], list[-1]]
newfirstlist = take_number(a)
print(newfirstlist)
newsecondlist = take_number(b)
print(newsecondlist)
"""
"""
def gen_fib():
    count = int(input("How many fibonacci numbers would you like to generate? "))
    i = 1
    if count == 0:
        fib = []
    elif count == 1:
        fib = [1]
    elif count == 2:
        fib = [1,1]
    elif count > 2:
        fib = [1,1]
        while i < (count - 1):
            fib.append(fib[i] + fib[i-1])
            i += 1

    return fib
"""
"""
file = "names.txt"
names_dict = dict()
newlist = list()
def file_open(file_name):
    listnames = list()
    with open(file_name) as open_file:
        lines = open_file.readlines()
        #print(lines)
        for word in lines:
            name = word.rstrip()
            listnames.append(name)
    return listnames

#print(file_open(file))
newlist = file_open(file)
for i in newlist:
    count = 1
    if i in names_dict:
        names_dict[i] += 1
    else:
        names_dict[i] = 1

print(names_dict)
"""
"""
dictionary = {}
key = "key"
value = 2
print(type(dictionary))
dictionary[key] = value
print(dictionary)
dictionary = {"a" : 3}
print(dictionary)
print(type(dictionary))
"""
"""
numbers1 = "numbers1.txt"
numbers2 = "numbers2.txt"

def file_open(file_name):
    with open(file_name) as open_file:
        numberlist=list()
        lines = open_file.readlines()
        for number in lines:
            num = number.rstrip()
            #print(num)
            numberlist.append(num)
        #print(numberlist)
    return numberlist

def main():
    overlapping = list()
    new_number1 = file_open(numbers1)
    new_number2 = file_open(numbers2)
    for i in new_number1:
        if new_number1[i] in new_number2:
            overlapping.append(new_number1[i])
        i+=1
    print(overlapping)

if __name__ == "__main__":
        main()
"""
"""
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
"""
"""
a = [2,3,7,3,2,6,8,3,5,234,46,765,2,34,89,567,234,63,45,653,34,23,556,234]
numbers = set()

for number in a:
    numbers.add(number)
print(numbers)
print(len(numbers))
"""
"""
numbers1 = "numbers1.txt"
numbers2 = "numbers2.txt"
def openfile(file_name):
    numlist = list()
    with open(file_name) as file_open:
        for line in file_open:
            numbers = line.rstrip().split()
            numlist.append(numbers)
        return numlist

def main():
    numbers1_list = openfile(numbers1)
    numbers2_list = openfile(numbers2)
    overlapping = list()
    for number in numbers1_list:
        if number in numbers2_list:
            overlapping.append(number)
    print(overlapping)

if __name__ == "__main__":
    main()
"""
"""
FILE = "names.txt"
def openfile(name_of_file):
    name_list = list()
    with open(name_of_file) as file_open:
        lines = file_open.readlines()
        for i in lines:
            names = i.rstrip()
            name_list.append(names)
        return name_list


def main():
    name_list = openfile(FILE)
    print(name_list)
    name_dict = dict()
    count = 1
    for i in name_list:
        if i not in name_dict:
            name_dict[i] = count
        else:
            count += 1
            name_dict[i] = count

    print(name_dict)

if __name__ == "__main__":
    main()
"""
"""
FILE = "names.txt"
list1= list()
list2= list()
list3= list()
list4= list()
list5= list()
list6= list()
def openfile(name_of_file):
    with open(name_of_file) as file_open:

        for i in file_open:
            list1.append(i)
            nam = i.rstrip()
            list2.append(nam)
            num = i.rstrip().split()
            list3.append(num)
        print("list1 = " , list1)
        print("list2 = " , list2)
        print("list3 = " , list3)

    with open(name_of_file) as open_file:
        lines = open_file.readlines()
        print("list4 = " , lines)
        for x in lines:
            y = x.rstrip()
            list5.append(y)
            z = x.rstrip().split()
            list6.append(z)
        print("list5 = " , list5)
        print("list6 = " , list6)

def main():
    openfile(FILE)
if __name__ == "__main__":
    main()
"""
"""
FILE = "birthdays.txt"
def openfile(name_of_file):
    bday_list = list()
    with open(name_of_file) as file_open:
        lines = file_open.readlines()
        for i in lines:
            bdays = i.rstrip().split()
            bday_list.append(bdays)
    return bday_list

def main():
    bday_dict = dict()
    bday_list = openfile(FILE)
    #print(bday_list)

    for i in range(0, len(bday_list)):
        bday_dict[bday_list[i][0]] = bday_list[i][1]
        i +=1
    #print(bday_dict)

    print("Welcome to birthday dictionary. We know the birthdays of:"
          "Zeynep"
          "Ali"
          "Zeren"
          "Deniz"
          "Asli"
          "Ayfer"
          "Cemal"
          "Sevde"
          "Shawn"
          "Resat")
    name = input("Who's birthday you would like to know?: ")
    print(f"{name}'s birthday is {bday_dict[name]}.")

if __name__ == "__main__":
    main()
"""
