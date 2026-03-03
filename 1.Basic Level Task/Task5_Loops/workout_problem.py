'''Imagine you are doing a workout routine, and you have to complete 100
jumping jacks.
Write a program that:
Asks you to perform 10 jumping jacks at a time.
After each set, it asks, "Are you tired?"
If you reply "yes" or "y," it should ask if you want to skip the remaining sets.
If you reply "yes" or "y," it should break and print, "You completed a total of
jumping jacks."'''

import sys 
import time 

total_jacks = 0 
target_jacks = 100 
set = target_jacks // 10 

print(f"lets Start Your Jumping Jacks Workout! You need to complete total {target_jacks} jumping jacks.")

for set_num in range (set) :
    
    for i in range(1,11):
        print(f"{i} Jumps ", end = "\r")
        sys.stdout.flush()
        time.sleep(0.5)


    total_jacks +=10
    print(f'\n Set complete Total : {total_jacks} , Total Left {target_jacks - total_jacks} Jumping Jacks ')

    tired = input("Are You Tried ?(Yes or No):") .strip().lower()
    
    if tired in ['yes', 'y' ] :
        skip = input("Do You Want to Skip remaining Sets ? ").strip().lower()
        if skip in ['yes', 'y']:
            break
    remaining = target_jacks - total_jacks
    if remaining >0 :
        print(f"Great Job! {remaining} Jumpping Jacks reamining .")

if total_jacks >= target_jacks:
    print(f"Congratulation! You Complete the Workout of {target_jacks} Jumping Jacks .")
else :
    print(f"You complete a total of {total_jacks} Jumping Jacks.")