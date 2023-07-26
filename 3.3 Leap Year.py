print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
small = 15
medium = 20
large = 25
pepperoni = 3
small_pepperoni = 2
cheese = 1

# For Small pizza#####################################
if size == 'S' and add_pepperoni == 'Y' and extra_cheese == 'Y':
    print(f"Your final bill is: ${small + small_pepperoni + cheese}.")

if size == 'S' and add_pepperoni == 'Y' and extra_cheese == 'N':
    print(f"Your final bill is: ${small + small_pepperoni}.")

if size == 'S' and add_pepperoni == 'N' and extra_cheese == 'Y':
    print(f"Your final bill is: ${small + cheese}.")

if size == 'S' and add_pepperoni == 'N' and extra_cheese == 'N':
    print(f"Your final bill is: ${small}.")
    
# For Medium pizza######################################
if size == 'M' and add_pepperoni == 'Y' and extra_cheese == 'Y':
    print(f"Your final bill is: ${medium + pepperoni + cheese}.")

if size == 'M' and add_pepperoni == 'Y' and extra_cheese == 'N':
    print(f"Your final bill is: ${medium + pepperoni}.")
    
if size == 'M' and add_pepperoni == 'N' and extra_cheese == 'Y':
    print(f"Your final bill is: ${medium + cheese}.")

if size == 'M' and add_pepperoni == 'N' and extra_cheese == 'N':
    print(f"Your final bill is: ${medium}.")


# For Large pizza##########################################    
if size == 'L' and add_pepperoni == 'Y' and extra_cheese == 'Y':
    print(f"Your final bill is: ${large + pepperoni + cheese}.")

if size == 'L' and add_pepperoni == 'Y' and extra_cheese == 'N':
    print(f"Your final bill is: ${large + pepperoni}.")

if size == 'L' and add_pepperoni == 'N' and extra_cheese == 'Y':
    print(f"Your final bill is: ${large + cheese}.")

if size == 'L' and add_pepperoni == 'N' and extra_cheese == 'N':
    print(f"Your final bill is: ${large}.")

############################################
