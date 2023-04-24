# https://www.w3resource.com/python-exercises/file/python-io-exercise-8.php

FILE = "text.txt"
def read_file(file_name):
    line_list = list()
    with open(file_name) as open_file:
        read = open_file.readlines()
        for i in read:
            line = i.rstrip().replace(","," ")       
            line = line.split()
            line_list.append(line)
        return line_list

def main():
    linelist = list()
    lengthlist = list()
    line_list = read_file(FILE)
    for sentence in line_list:
        #print(sentence)

        for j in sentence:
            l = len(j) , j

            lengthlist.append(l)
    print(type(l))
    M = max(lengthlist)
    print(M[1])

if __name__ == "__main__":
    main()
