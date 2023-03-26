#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator")
the_bill = float(input("What was the total bill? "))
percentage_tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people_count = int(input("How many people to split the bill? "))

tip_to_pay = (percentage_tip / 100) * the_bill;
total_bill = the_bill + tip_to_pay
bill_per_person = round(total_bill / people_count, 2)

final_message = f"Each person should pay: ${bill_per_person}"

# print the final amount each person should page
print(final_message )
