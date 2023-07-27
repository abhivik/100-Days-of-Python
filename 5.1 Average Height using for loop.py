## Average Height: Using for loop ##

# write a program that calculates the average student height from a List of heights.

student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
#print(student_heights)

total_height = 0
for height in student_heights:
    total_height += height
#print(total_height)
count = 0
for number in student_heights:
    count += 1
    #print(count)
print(round(total_height/count))

