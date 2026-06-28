# Read inventory data from file and return it as a dictionary
def read_file(file_name):
    products = {}

    try:
        with open(file_name, "r") as sales_file:
            for line in sales_file:
                line = line.strip()

                if line:
                    product_name, quantity = line.split(" - ")
                    products[product_name] = int(quantity)

    except FileNotFoundError:
        print("Inventory file not found. Starting with an empty inventory.")

    return products


# Save inventory data to file
def save_file(file_name, products):
    with open(file_name, "w") as sales_file:
        for product_name, quantity in products.items():
            sales_file.write(f"{product_name} - {quantity}\n")


# Load products from file
products = read_file("sales_file.txt")


while True:

    user_request = input("""
==============================
 Inventory Management System
==============================

1. Add Product
2. Sell Product
3. Search Product
4. Show All Products
5. Save Data
6. Inventory Report
7. Exit

Enter your choice: """)

    # Exit program
    if user_request.strip() == "7" or user_request.lower().strip() == "exit":
        save_file("sales_file.txt", products)
        print("Data saved. Goodbye!")
        break

    # Add product
    elif user_request.strip() == "1" or user_request.lower().strip() == "add":

        product_name = input(
            "Enter product name: "
        ).lower().strip()

        try:
            if product_name in products:

                print(
                    f"Product already exists.\n"
                    f"Current quantity: {products[product_name]}"
                )

                quantity = int(
                    input("Enter quantity to add: ")
                )

                if quantity < 0:
                    print("Quantity cannot be negative.")
                    continue

                products[product_name] += quantity

                print(
                    f"Quantity updated successfully.\n"
                    f"New quantity: {products[product_name]}"
                )

            else:

                quantity = int(
                    input("Enter product quantity: ")
                )

                if quantity < 0:
                    print("Quantity cannot be negative.")
                    continue

                products[product_name] = quantity

                print(
                    f"Product '{product_name}' added successfully.\n"
                    f"Quantity: {quantity}"
                )

        except ValueError:
            print("Please enter a valid number.")

    # Sell product
    elif user_request.strip() == "2" or user_request.lower().strip() == "sell":

        product_name = input(
            "Enter product name to sell: "
        ).lower().strip()

        if product_name in products:

            print(
                f"Available quantity: "
                f"{products[product_name]}"
            )

            try:
                quantity = int(
                    input("Enter quantity to sell: ")
                )

                if quantity <= 0:
                    print("Quantity must be greater than zero.")
                    continue

                if quantity <= products[product_name]:

                    products[product_name] -= quantity

                    if products[product_name] == 0:

                        del products[product_name]

                        print(
                            f"'{product_name}' is out of stock.\n"
                            f"Product removed from inventory."
                        )

                    else:

                        print(
                            f"Sale completed successfully.\n"
                            f"Remaining quantity: "
                            f"{products[product_name]}"
                        )

                else:

                    print(
                        f"Not enough stock available for "
                        f"'{product_name}'."
                    )

                    print(
                        f"Current quantity: "
                        f"{products[product_name]}"
                    )

            except ValueError:
                print("Please enter a valid number.")

        else:
            print(
                f"Product '{product_name}' does not exist."
            )

    # Search product
    elif user_request.strip() == "3" or user_request.lower().strip() == "search":

        product_name = input(
            "Enter product name to search: "
        ).lower().strip()

        if product_name in products:

            print(
                f"{product_name}: "
                f"{products[product_name]}"
            )

        else:
            print("Product not found.")

    # Show all products
    elif user_request.strip() == "4" or user_request.lower().strip() == "show":

        if products:

            print("\nCurrent Inventory")
            print("-----------------")

            for product_name, quantity in products.items():
                print(f"{product_name} - {quantity}")

        else:
            print("Inventory is empty.")

    # Save data
    elif user_request.strip() == "5" or user_request.lower().strip() == "save":

        save_file("sales_file.txt", products)

        print("Data saved successfully.")

    # Inventory report
    elif user_request.strip() == "6" or user_request.lower().strip() == "report":

        if products:

            max_product = max(products, key=products.get)
            min_product = min(products, key=products.get)

            print(f"""
==============================
      Inventory Report
==============================

Number of Products : {len(products)}
Total Quantity     : {sum(products.values())}

Highest Stock:
    {max_product} ({products[max_product]})

Lowest Stock:
    {min_product} ({products[min_product]})
""")

        else:
            print("Inventory is empty.")

    # Invalid menu option
    else:
        print(
            "Invalid option. Please select a number between 1 and 7."
        )