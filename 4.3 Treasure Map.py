## Treasure Map ##
# WAP that will mark the spot "x" in 3x3 matrix
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? Enter 2 digit number consisting only of 1, 2, and 3: ")

#Write your code below this row 👇
horizontal = int(position[0])
vertical = int(position[1])

map[vertical-1][horizontal-1] = "X"


print(f"{row1}\n{row2}\n{row3}")