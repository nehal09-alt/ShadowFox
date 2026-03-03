#1. You have a list of superheroes representing the Justice League :



justice_league =["Superman" , "Batman", "Wonder Woman" , "Flash", "Aqua Man" , "Green Lantern" ] 

#Perform the following tasks:


#1. Calculate the number of members in the Justice League.

print("Q.1}")
count = len(justice_league)
print(f'''The total member of Justice League is {count}''')

print("\n")

#2. Batman recruited Batgirl and Nightwing as new members.  Add them to your list.

print("Q.2}")
justice_league_copy = justice_league.copy()
justice_league_copy[1] = "Batgirl"
print(justice_league_copy)

justice_league_copy.append("Nightwing")
print(justice_league_copy)

print("\n")


#3. Wonder Woman is now the leader of the Justice League. Move her to the beginning of the list.

print("Q.3}")

justice_league_copy.remove("Wonder Woman")
justice_league_copy.insert(0,"Wonder Woman")
print(justice_league_copy)
print("\n")

#4. Aquaman and Flash are having conflicts, and you need to separate them. Choose either "Green Lantern" or "Superman" and move them in between Aquaman and Flash.
print("Q.4}")
justice_league_copy.remove ("Superman")
flash_index = justice_league_copy.index("Flash")
Aquaman_index = justice_league_copy.index("Aqua Man")

Position = min(flash_index,Aquaman_index) +1 

justice_league_copy.insert(Position, "Superman")

print(justice_league_copy)

print("\n")

#5. The Justice League faced a crisis, and Superman decided to assemble a new team. Replace the existing list with the following new members:
#  "Cyborg","Shazam","Hawkgirl","Martian Manhunter","Green Arrow".

print('Q.5}')

del justice_league[1:]

justice_league_New =["Cyborg","Shazam","Hawkgirl","Martian Manhunter","Green Arrow"]

justice_league.extend(justice_league_New)

print(justice_league)
print("\n")

#6. Sort the Justice League alphabetically. The hero at the 0th index will become the new leader.

print("Q.6}")

old_alphabetic_order = sorted(justice_league_copy)

alphabetic_order = sorted(justice_league)

print(f'''For Old List given .The Alphabetic order should be :- {old_alphabetic_order}''')
print(f'''For New List.The Alphabetic order sahould be :- {alphabetic_order}''')

print("\n")

#7. BONUS  Question : 
# Can you predict who the new leader will be ?

print("BONUS QUESTION")

New_leader =old_alphabetic_order[0]
New_leader_new = alphabetic_order[0]

print(f'''The New Leader of Old List is {New_leader}''')

print(f'''The New Leader of New List is {New_leader_new}''')