# https://www.practicepython.org/exercise/2014/12/06/22-read-from-file.html
# File can be found in link at the website.

file = "names.txt"
names_dict = dict()
newlist = list()
def file_open(file_name):
    listnames = list()
    with open(file_name) as open_file:
        lines = open_file.readlines()
        for word in lines:
            name = word.rstrip()
            listnames.append(name)
    return listnames
