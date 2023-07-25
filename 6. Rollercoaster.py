# Can ride a rollercoaster above 120cm height.
# Price per age: 12 and younger = $5, Above 12 and below 18 = $7, Above 18 = $12
# If want pictures to be taken = $3
 
height = int(input("Please enter your height: "))
bill = 0

if height >=120:
    print("You can ride the rollercoaster!")
    age = int(input("Please enter your age: "))
    if age < 12:
        bill += 5
        print("Child tickets are $5.")
    elif age >= 12 and age <= 18:
        bill += 7
        print("Youth tickets are $7.")
    else:
        bill += 12
        print("Adult tickets are $12.")
    
    photos = input("Do you want photos? Y/N: ")
    photos = photos.lower()
    if photos == "y":
        bill += 3
    print(f"The total bill is ${bill}.")

else:
    print("Sorry. You cannot ride.")

