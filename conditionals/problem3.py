# Grade Calculator
#Assign a letter grade based on a student's score :
# A (90-100), B(80-89), C(70-79), D(60-69), F(<60)

score = 1
if score >=101:
    print("Please verify your grade")
    exit()
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
elif score >= 50:
    grade = "E"
else:
    grade = "F"

print("Grade: ", grade)