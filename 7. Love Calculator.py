## Love Calculator ##
# write a program that tests the compatibility between two people.

# To work out the love score between two people:
# Take both people's names and check for the number of times the letters in the word TRUE occurs. 
# Then check for the number of times the letters in the word LOVE occurs. 
# Then combine these numbers to make a 2 digit number.


print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name = (name1 + name2)
name = name.lower()

t = name.count("t")
r = name.count("r")
u = name.count("u")
e = name.count("e")
true = t + r + u + e

l = name.count("l")
o = name.count("o")
v = name.count("v")
e = name.count("e")
love = l + o + v + e

love_score = int(str(true) + str(love))

# For Love Scores less than 10 or greater than 90
if love_score < 10 and love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")

# For Love Scores between 40 and 50
elif love_score > 40 and love_score < 50:
    print(f"Your score is {love_score}, you are alright together.")

# Otherwise
else:
    print(f"Your score is {love_score}.")
