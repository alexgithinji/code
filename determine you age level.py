def determine_age_category(age):
    if age >= 18:
        return "adult"
    else:
        return "child"

def main():
    try:
        age = int(input("Please enter your age: "))
        if age < 0:
            print("Invalid age. Age cannot be negative.")
        else:
            age_category = determine_age_category(age)
            print(f"You are classified as a {age_category}.")
    except ValueError:
        print("Invalid input. Please enter a valid age.")

if __name__ == "__main__":
    main()
