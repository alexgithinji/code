class Student:
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def calculate_average(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

def main():
    students = []

    while True:
        print("\nCampus Grading System")
        print("1. Add Student")
        print("2. Add Grade")
        print("3. Calculate Average")
        print("4. Display Student Info")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter student name: ")
            roll_number = input("Enter roll number: ")
            student = Student(name, roll_number)
            students.append(student)
            print("Student added!")

        elif choice == "2":
            roll_number = input("Enter roll number: ")
            grade = float(input("Enter grade: "))
            found = False
            for student in students:
                if student.roll_number == roll_number:
                    student.add_grade(grade)
                    print("Grade added!")
                    found = True
                    break
            if not found:
                print("Student not found!")

        elif choice == "3":
            roll_number = input("Enter roll number: ")
            found = False
            for student in students:
                if student.roll_number == roll_number:
                    average = student.calculate_average()
                    print(f"Average grade for {student.name}: {average:.2f}")
                    found = True
                    break
            if not found:
                print("Student not found!")

        elif choice == "4":
            for student in students:
                print(f"Name: {student.name}, Roll Number: {student.roll_number}")

        elif choice == "5":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()















