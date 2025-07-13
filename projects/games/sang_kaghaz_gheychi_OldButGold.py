import random
emtiyaz = 0
entekhabesystemstring = ""
while (True):
    print(" emtiyaz : " + str(emtiyaz))
    entekhab = input("1- sang \n2- kaghaz \n3- gheychi \n ")
    entekhab = int(entekhab)
    if entekhab == 0:
        break
    if (entekhab != 1) and (entekhab != 2) and (entekhab != 3):
        print(" voroodi na motabar ast ")
        break
    entekhabesystem = random.randint(1, 3)
    if entekhabesystem == 1:
        entekhabesystemstring
    elif entekhabesystem == 2:
        entekhabesystemstring
    elif entekhabesystem == 3:
        entekhabesystemstring
    print(" entekhabe system : " + entekhabesystemstring)
    if (entekhabesystem == 1 and entekhab == 2) or (entekhabesystem == 2 and entekhab == 3) or (entekhabesystem == 3 and entekhab == 1):
        print(" shoma barande shodid \a!!! ")
        emtiyaz += 1
    elif entekhabesystem == entekhab:
        print(" mosavi shodid !! ")
    else:
        print(" shoma bakhtid !!! ")
        emtiyaz -= 1
    print(" \n\n ")
#MadMad_30