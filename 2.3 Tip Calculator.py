## Tip Calculator ##
# Split a bill between individuals with included tip of 5%, 12%, and 15% included.
# If the bill was $150.00, split between 5 people, with 12% tip. 
# Each person should pay (150.00 / 5) * 1.12 = 33.6

print("Welcome to the tip calculator.")

#Take inputs
bill = float(input("What was your total bill? $"))
percentage = int(input("What percentage of bill would you like to give? 10, 12, or 15? "))

#Calculating the tip in percentage.
tip = float(bill*percentage/100)
people = int(input("How many people are splitting the bill? "))

#Add the bill with tip and divide it among the number of people.
#Format the result to 2 decimal places = 33.60
bill_div = (bill + bill*percentage/100)/7

#Print the output with total bill which included tip and splitted as per number of people.
print(f"Each person should pay: ${round(bill_div})")
