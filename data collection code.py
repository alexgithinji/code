name = input("What is your name? ")
age = int(input("How old are you? "))
location = input("Where are you located? ")

if age >= 18:
    print(f"Hello, {name}! Since you are {age} years old and located in {location}, you are eligible to vote.")
else:
    print(f"Hello, {name}! Unfortunately, you are not yet eligible to vote since you are {age} years old.")
