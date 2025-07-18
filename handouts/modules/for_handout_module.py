'''
module is a normal python script can import that
in main file and use it's functions '''

if (__name__ == "__main__"):
    print("you should use this file as a module")

def whats_my_name_from_mo():
    print({__name__})

def imported_with_from():
    print("this function ruined from module with from syntax")

def imported():
    print("this function ruined from module with normal import syntax")

def count_char(s, c):
    founded = 0
    for this_char in s:
        if this_char == c:
            founded+=1
    return founded

PiNumber = 3.14

#print(f"in the module my name is {__name__}")
#MadMad_27