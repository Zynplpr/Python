# https://www.w3resource.com/python-exercises/file/python-io-exercise-9.php

FILE = "text.txt"
def read_file (file_name):
    file_list = list()
    with open(file_name) as open_file:
        sentence = open_file.readlines()
        for line in sentence:
            lines = line.rstrip()
            file_list.append(lines)
        return file_list

def main():
    file_list = read_file(FILE)
    length = len(file_list)
    print(length)

if __name__=="__main__":
    main()
