# Define the menu items with prices
menu = {
    "Burger": 500.99,
    "Pizza": 767.99,
    "Pasta": 634.99,
    "Salad": 423.99,
    "Soda": 11.99,
    "Water": 10.99
}

# Function to display the menu
def display_menu():
    print("=== Menu ===")
    for item, price in menu.items():
        print(f"{item}: ${price:.2f}")
    print("============")

# Function to take the user's order
def take_order():
    order = []
    while True:
        display_menu()
        choice = input("Enter the item you want to order (or 'done' to finish): ").strip().title()

        if choice == 'Done':
            break

        if choice in menu:
            order.append((choice, menu[choice]))
        else:
            print("Invalid choice. Please select a valid item from the menu.")

    return order

# Function to calculate the total cost of the order
def calculate_total(order):
    return sum(item[1] for item in order)

# Function to generate and print the receipt
def generate_receipt(order, total):
    print("\n=== Hotel Receipt ===")
    print("=====================")
    for item, price in order:
        print(f"{item}: ${price:.2f}")
    print("=====================")
    print(f"Total: ${total:.2f}")
    print("=====================")

# Main program
def main():
    print("Welcome to the hotel!")
    order = take_order()
    total = calculate_total(order)
    generate_receipt(order, total)
    print("Thank you for dining with us!")

if __name__ == "__main__":
    main()
