'''2. Write a program to determine which country a city belongs to. Given
list of cities per country:

Australia = ["Sydney","Melbourne","Brisbane","Perth"]

UAE = ["Dubai","Abu Dhabi","Sharjah","Ajman"]

India = ["Mumbai","Bangalore","Chennai","Delhi"]  

Ask the user to enter a city name and print the corresponding country.
Example:
Enter a city name: "Abu Dhabi"
Output: "Abu Dhabi is in UAE"'''

Australia = ["Sydney","Melbourne","Brisbane","Perth"]

Uae  = ["Dubai","Abu Dhabi","Sharjah","Ajman"]

India = ["Mumbai","Bangalore","Chennai","Delhi"] 

city = input("Enter your City :- ")

if city in Australia :
    print(f''' {city}  in Australia ''')
elif city in Uae :
    print(f''' {city}  in Uae ''')
elif city in India :
    print(f''' {city}  in India ''')
else :
    print("City Not Found in given Country list ")
    