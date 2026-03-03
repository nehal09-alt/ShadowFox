'''1.Avengers is a Marvel’s American Superheroes team, Now you want to
showcase your programming skills by representing the Avengers team using
classes. Create a class called Avenger and create these six superheroes using this
class.
2. super_heroes = ["Captain America", "Iron Man", "Black Widow", "Hulk",
"Thor", "Hawkeye"]
3. Your Avenger class should have these properties:
1. Name
2. Age
3. Gender
4. Super Power
5. Weapon
4. Captain America has Super strength, Iron Man has Technology, Black Widow
is superhuman, Hulk has Unlimited Strength, Thor has super Energy and
Hawkeye has fighting skills as superpowers.
5. Weapons: Shield, Armor, Batons, No Weapon for hulk, Mjölnir, Bow, and
Arrows
6. Create methods to get the information about each superhero
7. Create a method is_leader() which will tell if the superhero is a leader or not.'''

class Avenger :
    def __init__(self , Name , Age , Gender , Super_Power , Weapon):
        self.Name = Name
        self.Age = Age
        self.Gender = Gender
        self.Super_Power = Super_Power
        self.Weapon =Weapon

    def info(self):
        print(f'Name : {self.Name}') 
        print(f'Age: {self.Age}')
        print(f'Gender : {self.Gender}')
        print(f'Super Power Of {self.Name} is  : {self.Super_Power}')
        print(f'Weapon of {self.Name} is  : {self.Weapon}')
   
    def Leader (self):
        if self.Name == 'Captain America':
            print(f'{self.Name} is the Leader of Avegers Team ')
        else: print(f'{self.Name} is not a Leader of Avenger Team')
        
avenger1 = Avenger("Captain America" , 100 , 'Male' , 'Super Strength' , 'Sheild')
avenger2 = Avenger('Iron Man' , 36 , 'Male' , 'Technology' , 'Armor')
avenger3 = Avenger('Black Widow ', 30 , 'Female' , 'SuperHuman' , 'Batons')
avenger4 = Avenger('Hulk' , 52 , 'Male' , 'Unlimmited Strength' , 'No Weapon')
avenger5 = Avenger('Thor' , 200 , 'Male' ,'Super Energy' , 'Mjolnir')
avenger6 = Avenger('Hawkeye' , 44 , 'Male','fighting Skills and SuperPowers' , 'Arrows and Bows')

Avengers = [avenger1 , avenger2 ,avenger3 , avenger4 , avenger5 ,avenger6]

for Hero in Avengers :
    print("----------------------------------------------------------------")
    Hero.info()
    Hero.Leader()
    print('------------------------------------------------------------------')