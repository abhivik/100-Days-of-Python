## Highest Score using for loop ##

# Write a program that calculates the highest score from a List of scores.

student_scores = input("Enter the list of student scores: ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])

highest_score = student_scores[0]
for score in student_scores:
    if score > highest_score:
        highest_score = score
print("The highest score in the class is: ",highest_score)
