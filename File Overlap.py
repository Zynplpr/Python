# https://www.practicepython.org/exercise/2014/12/14/23-file-overlap.html

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
