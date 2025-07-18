while True:
    NumToCal1 = input('\n\nenter the first number : ')
    if(NumToCal1.isdigit()):
        Op = input("\n1.'+'\n2.'-'\n3.'*'\n4.'/'\n5.'exit'\n>> ")
        if((Op=='exit') or (Op=='5')):
            break
        NumToCal2 = input('\nenter the second number : ')
        if(NumToCal2.isdigit()):
            match Op:
                case '+' | '1':
                    print(f'\n{NumToCal1} + {NumToCal2} = {int(NumToCal1)+int(NumToCal2)}')
                case '-' | '2':
                    print(f'\n{NumToCal1} - {NumToCal2} = {int(NumToCal1)-int(NumToCal2)}')
                case '*' | '3':
                    print(f'\n{NumToCal1} * {NumToCal2} = {int(NumToCal1)*int(NumToCal2)}')
                case '/' | '4':
                    print(f'\n{NumToCal1} / {NumToCal2} = {int(NumToCal1)/int(NumToCal2)}')
                case _:
                    print("\ninvalid operation..\n")
                    continue
#MadMad_21