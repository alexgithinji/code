def calculate_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'


def main():
    num_students = int(input("Enter the number of students: "))

    student_data = []
    for i in range(num_students):
        name = input(f"Enter name of student {i + 1}: ")
        score = int(input(f"Enter score for {name}: "))
        grade = calculate_grade(score)
        student_data.append((name, score, grade))

    print("\nStudent Report:")
    print("Name\tScore\tGrade")
    print("-------------------")
    for name, score, grade in student_data:
        print(f"{name}\t{score}\t{grade}")


if __name__ == "__main__":
    main()
