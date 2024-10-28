#take input of average marks from user
marks = float(input("Enter the average marks: "))

#check the grade based on marks

if marks >= 90:
    grade = "A+"
elif marks >= 70:
    grade = "A-"
elif marks >= 50:
    grade = "B"
else:
    grade = "Fail"
    
print("Your grade is : ", grade)