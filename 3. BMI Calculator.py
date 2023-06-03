#  A program that interprets the Body Mass Index (BMI) based on a user's weight and height.
#It tells them the interpretation of their BMI based on the BMI value.

# Take input values for height and weight
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

# Calculate the BMI and limit the decimal place to 2
bmi = round(weight/height**2)

#Under 18.5 they are underweight
if bmi < 18.5: 
    print(f"Your BMI is {bmi}, you are underweight.") 

#Over 18.5 but below 25 they have a normal weight
elif bmi < 25: 
    print(f"Your BMI is {bmi}, you have normal weight.")

#Over 25 but below 30 they are slightly overweight
elif bmi < 30: 
    print(f"Your BMI is {bmi}, you are slightly over weight.")

#Over 30 but below 35 they are obese
elif bmi < 35: 
    print(f"Your BMI is {bmi}, you are obese.")

#Above 35 they are clinically obese.
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")
