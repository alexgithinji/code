"""while True:
    name=input("enter your name")
    if name !="":
        break"""
rows = int(input("how many rows?:"))
columns = int(input("how many columns?:"))
symbol = input("enter a symbol to use:")

for i in range(rows):
    for j in range(columns):
        print(symbol, end="")
    print()
#indentation can cause an wrong output
