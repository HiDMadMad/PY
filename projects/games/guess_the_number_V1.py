from math import inf
import random


wanted_to_play_again = True
record = inf

while(wanted_to_play_again):
    difficulty = input("\n1.easy\n2.medium\n3.hard\n4.iran mode\n5.exit\n>>  ")
    match difficulty:
        case '1' | 'easy':
            initial_guess_num=4
            start_of_range=1
            end_of_range=20
            bot_num=random.randint(start_of_range, end_of_range)
        case '2' | 'medium':
            initial_guess_num=5
            start_of_range=1
            end_of_range=50
            bot_num=random.randint(start_of_range, end_of_range)
        case '3' | 'hard':
            initial_guess_num=6
            start_of_range=1
            end_of_range=100
            bot_num=random.randint(start_of_range, end_of_range)
        case '4' | 'iran mode':
            initial_guess_num=7
            start_of_range=1
            end_of_range=251
            bot_num=random.randint(start_of_range, end_of_range)
        case '5' | 'exit':
            break
        case _:
            print("\nchoose between 1 to 5")
            continue

    player_foundation = False
    guess_num = initial_guess_num

    print(f"\nmy number is between of {start_of_range} to {end_of_range}\nyou have {guess_num} chooses\n")
    while(guess_num>0):
        try:
            player_guess = int(input("\ninput your guess : "))
        except ValueError:
            print("enter a number nooob!!\n")
            continue

        if(player_guess==bot_num):
            record = (initial_guess_num-guess_num+1) if ((initial_guess_num-guess_num)<record) else record
            print(f"\ngg you got me! WP <3\nyou found it with {initial_guess_num-guess_num+1} guesses!\nrecord is {record}\n")
            player_foundation=True
            break
        elif(player_guess>bot_num):
            print("my number is lower than yours")
            guess_num-=1
            print(f"you have {guess_num} chooses\n")
        else:
            print("my number is higher than yours")
            guess_num-=1
            print(f"you have {guess_num} chooses\n")
    if(not player_foundation):
        print(f"ha ha ha looooser =))))))\nmy number is {bot_num} =((((")
        if(record!=inf):
            print("\nrecord is {record}.\n")

    to_continue = input("\ndo you want to play again? (Y/N)\n>>")
    if(to_continue.upper() in ['Y', 'YES', 'ARE', 'BALE']):  # to_continue=='Y' or to_continue=='y'   OR   to_continue.upper() == 'Y'
        wanted_to_play_again = True
    else:
        wanted_to_play_again = False
        print("\n\nhave a good time body <3 \n\n")
#MadMad_72