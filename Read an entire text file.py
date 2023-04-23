# https://www.w3resource.com/python-exercises/file/python-io-exercise-1.php

FILE = "text.txt"
def file_open(file_name):
    with open(file_name) as open_file:
        lines = open_file.readlines()
        for i in lines:
            line = i.rstrip()
            print(line)

file_open(FILE)
