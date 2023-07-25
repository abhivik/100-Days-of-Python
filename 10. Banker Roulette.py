## Banker Roulette ##
# Write a program that will select a random name from list of names.
# The person selected will have to pay for everybody.

import random

name_list = input("Enter the names seperated by comma: ")
names = name_list.split(", ")

total_names = len(names)
random_name = random.randint(0, total_names - 1)
person_paying = names[random_name]
print(f"{person_paying} is going to buy the meal today")