# https://www.practicepython.org/exercise/2014/12/06/22-read-from-file.html
# File can be found in link at the website.

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
