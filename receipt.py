# Function to calculate the total cost
def calculate_total(items):
    total = sum(item['price'] for item in items)
    return total


# Function to generate and print the receipt
def generate_receipt(items, total):
    print("\n=== Hotel Receipt ===")
    print("====================")
    for item in items:
        print(f"{item['name']:20} {item['price']:.2f}")
    print("====================")
    print(f"Total:              {total:.2f}")
    print("====================")


# Main program
def main():
    items = []

    while True:
        name = input("Enter item name (or 'done' to finish): ")
        if name.lower() == 'done':
            break
        price = float(input("Enter item price: "))
        items.append({'name': name, 'price': price})

    total = calculate_total(items)
    generate_receipt(items, total)


if __name__ == "__main__":
    main()






