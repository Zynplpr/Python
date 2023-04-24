# https://www.w3resource.com/python-exercises/file/python-io-exercise-10.php

FILE = "text.txt"
def read_file(file_name):
    file_list = list()
    with open(file_name) as open_file:
        sentence = open_file.readlines()
        for i in sentence:
            line = i.rstrip().replace("," , " ")
            lines = line.split()
            file_list.append(lines)

    return file_list

def main():
    file_list = read_file(FILE)
    file_dict = dict()
    for i in file_list:
        count = 1
        for word in i:
            if word in file_dict:
                count += 1
                file_dict[word] = count
            else:
                file_dict[word] = count
    print(file_dict)

if __name__ == "__main__":
    main()
