## Life In Weeks ##
# Create a program using maths and f-Strings that tells us
# how many days, weeks, months we have left if we live until 90 years old.
age = input("What is your current age? ")


#Write your code below this line 👇
years = 90 - int(age)
days = years * 365
weeks  = years * 52
months = years * 12
print(f"You have {days} days, {weeks} weeks, and {months} months left.") 