# Quick Pick Numbers generator for Powerball & Megamillions
# Author: Rajathithan Rajasekar
# Date: 03/23/2021

import random

my_seed_list = [*range(1,1001,1)]

def lotteryFunc(n,b,seed):
    list_num = []
    random.seed(seed)
    fivenums = [*range(1,n,1)]
    Mball = [*range(1,b,1)]

    while len(list_num) < 5:
        num = random.choice(fivenums)
        if num not in list_num:
            list_num.append(num)

    list_num.sort()
    ball = random.choice(Mball)
    
    return list_num, ball


for i in range(6):
    print("Enter the single alphabet in CAPS:")
    #lottery_type = input("Powerball- 'P' // Megamillions - 'M' // Exit - 'E' :\n")
    lottery_type = 'M'
    seed = random.choice(my_seed_list)

    if lottery_type == 'P':
        nums, ball = lotteryFunc(70,27,seed)
        print(f"Powerball Numbers - Quick Pick: {nums} - {ball}\n\n")

    elif lottery_type == 'M':
        nums, ball = lotteryFunc(71,26,seed)
        print(f"Megamillion Numbers - Quick Pick: {nums} - {ball}\n\n")

    elif lottery_type == 'E':
        print("\nThanks for using the lottery random number generator program")
        break

    else:
        print("\nTry again !!! Please enter proper input alphabet:")
        print("=================================================\n")
