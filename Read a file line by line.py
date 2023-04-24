# https://www.w3resource.com/python-exercises/file/python-io-exercise-5.php

FILE = "text.txt"
def read_file(file_name):
    line_list = list()
    with open(file_name) as open_file:
        line_list= open_file.readlines()
        print(line_list)
        
read_file(FILE)

# or by using .rstrip() \n and other spaces can be eliminated:

FILE = "text.txt"
def read_file(file_name):
    line_list = list()
    with open(file_name) as open_file:
        lines = open_file.readlines()
        for i in lines:
            new_line = i.rstrip()
            line_list.append(new_line)
        print(line_list)

read_file(FILE)
