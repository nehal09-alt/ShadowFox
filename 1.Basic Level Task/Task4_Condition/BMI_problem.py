'''1. Write a program to determine the BMI Category based on user input.
Ask the user to:
Enter height in meters
Enter weight in kilograms
Calculate BMI using the formula: BMI = weight / (height)2
Use the following categories:
If BMI is 30 or greater, print "Obesity"
If BMI is between 25 and 29, print "Overweight"
If BMI is between 18.5 and 25, print "Normal"
If BMI is less than 18.5, print "Underweight"
Example:
Enter height in meters: 1.75
Enter weight in kilograms: 70
Output: "Normal" '''

user_input = input("Enter you Name : ")

input_height = float(input(f'''Enter you Height in (meters) {user_input} :- '''))

input_weight = float(input(f'''Enter you Weight  in (Kilograms) {user_input} :- '''))

BMi_calc = input_weight / (input_height ** 2 )

if BMi_calc >= 30 :
    print(f'''{user_input} your BMI is {BMi_calc} --- Obesity''')
elif  BMi_calc >= 25:
    print(f'''{user_input} your BMI is {BMi_calc} --- OverWeight ''')
elif BMi_calc >= 18.5  :
    print(f'''{user_input} your BMI is {BMi_calc} --- Normal''')
else :
    print(f'''{user_input} your BMI is {BMi_calc} --- UnderWeight ''')



