# https://www.practicepython.org/exercise/2017/01/24/33-birthday-dictionaries.html
# I created a file with birthdays.
"""
Zeynep 02.11.2003
Ali 23.02.2002
Zeren 29.04.2009
Deniz 20.12.2002
Asli 10.12.2002
Ayfer 19.10.1968
Cemal 18.05.1964
Sevde 26.02.2002
Shawn 08.08.1998
"""

FILE = "birthdays.txt"
def openfile(name_of_file):
    bday_list = list()
    with open(name_of_file) as file_open:
        lines = file_open.readlines()
        for i in lines:
            bdays = i.rstrip().split()
            bday_list.append(bdays)
    return bday_list

def main():
    bday_dict = dict()
    bday_list = openfile(FILE)
    #print(bday_list)

    for i in range(0, len(bday_list)):
        bday_dict[bday_list[i][0]] = bday_list[i][1]
        i +=1

    print("Welcome to birthday dictionary. We know the birthdays of:"
          "Zeynep"
          "Ali"
          "Zeren"
          "Deniz"
          "Asli"
          "Ayfer"
          "Cemal"
          "Sevde"
          "Shawn"
          "Resat")
    name = input("Who's birthday you would like to know?: ")
    print(f"{name}'s birthday is {bday_dict[name]}.")

if __name__ == "__main__":
    main()
