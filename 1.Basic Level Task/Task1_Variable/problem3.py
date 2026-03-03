# 3. Store the principal amount, rate of interest, and time in different variables and then calculate the Simple Interest for 3 years. Formula: Simple Interest = P x R x T / 100

print("Problem 3 ")

principal_amount = float(input("Enter the Amount : "))
rate_of_interest = float(input("Enter the Rate of Interest : "))
time = float(input("Enter the time : "))

Simple_Interest = (principal_amount * rate_of_interest * time ) / 100 

print(f'''The Simple interest will be {Simple_Interest} of Amount : {principal_amount}  in Rate of Interest : {rate_of_interest}% at Time of {time} Years .''')
