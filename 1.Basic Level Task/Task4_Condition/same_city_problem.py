'''3. Write a program to check if two cities belong to the same country.
Ask the user to enter two cities and print whether they belong to the
same country or not.

Example:
Enter the first city: "Mumbai"
Enter the second city: "Chennai"
Output: "Both cities are in India"

Example:
Enter the first city: "Sydney"
Enter the second city: "Dubai"
Output: "They don't belong to the same country"'''

Australia = ["Sydney","Melbourne","Brisbane","Perth"]

Uae = ["Dubai","Abu Dhabi","Sharjah","Ajman"]

India = ["Mumbai","Bangalore","Chennai","Delhi"] 
 
input_city1 = input("Enter your First  City :- ").strip().title()
input_city2 = input("Enter your Second City :- ").strip().title()


if input_city1 in Australia and input_city2  in Australia :
    print (f'''The {input_city1} and {input_city2} They Belong to Same Country ''')

elif input_city1 in Uae and input_city2  in Uae :
    print (f'''The {input_city1} and {input_city2} They Belong to Same Country ''')

elif input_city1  in India and input_city2  in India :
    print (f'''The {input_city1} and {input_city2} They Belong to Same Country ''')

else :
    print(f'''{input_city1} and {input_city2} they don't belong the same Country ''')