# https://www.w3resource.com/python-exercises/file/python-io-exercise-18.php

FILE = "text.txt"
def read_file(file_name):
    file_list = list()
    with open(file_name) as open_file:
        line = open_file.readlines()
        for i in line:
            lines = i.rstrip().replace("," , " ")
            lines = lines.split()
            file_list.append(lines)
    return file_list

def main():
    file_list = read_file(FILE)
    word_list = list()
    for i in file_list:
        word_list.append(len(i))
    total = 0
    for i in word_list:
        total = i + total
    print(total)

if __name__=="__main__":
    main()
