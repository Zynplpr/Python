# https://www.w3resource.com/python-exercises/file/python-io-exercise-2.php

FILE = "text.txt"
def file_open(file_name):
    n = int(input("enter a number: "))
    with open(file_name) as open_file:
        i = 0
        while i < n:
            i += 1
            line = open_file.readline()
            lines = line.rstrip()
            print(lines)

file_open(FILE)
