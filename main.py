# Author: Grace Lavin gcl5087@psu.edu
# No Collaborator - HW
totalCredits = 0
#course 1
grade = input("Enter your course 1 letter grade: ")
if grade == "A" or grade == "a":
  gradeWeight = 4.
elif grade == "A-" or     grade == "a-":
  gradeWeight = 3.67
elif grade == "B+" or grade == "b+":
  gradeWeight = 3.33
elif grade == "B" or grade == "b":
  gradeWeight = 3.0
elif grade == "B-" or grade == "b-":
  gradeWeight = 2.67
elif grade == "C+" or grade == "c+":
  gradeWeight = 2.33
elif grade == "C" or grade == "c":
  gradeWeight = 2.00
elif grade == "D" or grade == "d":
  gradeWeight = 1.00
else:
  gradeWeight = 0.0
credit = input("Enter your course 1 credit: ")
print(f"Grade point for course 1 is: {gradeWeight}")
totalCredits = float(credit) + totalCredits
gradePoint1 = gradeWeight * float(credit)


#course 2
grade = input("Enter your course 2 letter grade: ")
if grade == "A" or grade == "a":
  gradeWeight = 4.
elif grade == "A-" or     grade == "a-":
  gradeWeight = 3.67
elif grade == "B+" or grade == "b+":
  gradeWeight = 3.33
elif grade == "B" or grade == "b":
  gradeWeight = 3.0
elif grade == "B-" or grade == "b-":
  gradeWeight = 2.67
elif grade == "C+" or grade == "c+":
  gradeWeight = 2.33
elif grade == "C" or grade == "c":
  gradeWeight = 2.00
elif grade == "D" or grade == "d":
  gradeWeight = 1.00
else:
  gradeWeight = 0.0

credit = input("Enter your course 2 credit: ")
totalCredits = float(credit) + totalCredits
gradePoint2 = gradeWeight * float(credit)
print(f"Grade point for course 2 is: {gradeWeight}")

#course 3
grade = input("Enter your course 3 letter grade: ")
if grade == "A" or grade == "a":
  gradeWeight = 4.
elif grade == "A-" or     grade == "a-":
  gradeWeight = 3.67
elif grade == "B+" or grade == "b+":
  gradeWeight = 3.33
elif grade == "B" or grade == "b":
  gradeWeight = 3.0
elif grade == "B-" or grade == "b-":
  gradeWeight = 2.67
elif grade == "C+" or grade == "c+":
  gradeWeight = 2.33
elif grade == "C" or grade == "c":
  gradeWeight = 2.00
elif grade == "D" or grade == "d":
  gradeWeight = 1.00
else:
  gradeWeight = 0.0

credit = input("Enter your course 3 credit: ")
print(f"Grade point for course 3 is: {gradeWeight}")
totalCredits = float(credit) + totalCredits
gradePoint3 = gradeWeight * float(credit)



#total gpa

GPA = (gradePoint1 + gradePoint2 + gradePoint3) / totalCredits
print(f"Your GPA is: {GPA}")



