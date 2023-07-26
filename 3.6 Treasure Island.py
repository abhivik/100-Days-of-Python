#Remember to use the random module
#Hint: Remember to import the random module here at the top of the file. 🎲
import random 
#Write the rest of your code below this line 👇
coin = 0,1
toss = random.choice(coin)
if toss == 0:
    print("Tails")
elif toss == 1:
    print("Heads")
