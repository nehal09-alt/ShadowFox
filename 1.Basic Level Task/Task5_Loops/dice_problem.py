'''1. Using a for loop, simulate rolling a sixsided die multiple times (at least 20
times).
Count and print the following statistics:
How many times you rolled a 6
How many times you rolled a 1
How many times you rolled two 6s in a row'''

import random

six_count = 0
one_count = 0 
double_six_count = 0 

rolls = []

n_roll = 20 

for i in range(n_roll):
    roll = random.randint(1,6)
    rolls.append(roll)

    if roll == 6 :
        six_count +=1 
    elif roll == 1 : 
        one_count +=1 

    if i > 0 and rolls[i-1] ==6 and roll ==6 :
        double_six_count+=1 
    

    print(f'''Roll {i+1} : {roll}''')

print(f'''\nWhen dice Roll {n_roll} times ''')
print(f'''\nSix rolled : {six_count}''')
print(f'''One Rolled : {one_count}''')
print(f'''Double Six Rolled : {double_six_count}''')