#takes user input
score = int(input("Enter your test score: "))

# Check the score and assign a grade using elif
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

# Display the grade
print(f"Your grade is: {grade}")
