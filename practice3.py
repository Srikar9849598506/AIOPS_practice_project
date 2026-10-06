coffee = {
    "Latte": 2.50,
    "Cappicuno": 3.00,
    "Espresso": 3.50
}


def home():

    print("\n==============================")
    print("     WELCOME TO COSTA COFFEE")
    print("==============================")

    while True:

        choice = input("Type 'start' to begin: ")

        if choice.lower() == "start":
            print("\nLet's get your coffee ready!")
            break

        else:
            print("Please type 'start' to start.")


def select_coffee():

    print("\nWhat does your mood say?")
    print("1. Latte")
    print("2. Cappicuno")
    print("3. Espresso")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        return "Latte"

    elif choice == 2:
        return "Cappicuno"

    elif choice == 3:
        return "Espresso"

    else:
        print("Invalid choice")
        return None


def quantity():

    n = int(input("Enter the quantity: "))

    return n


def get_price(coffee_name):

    return coffee[coffee_name]


def customise_coffee():

    print("\nWould you like to customise your coffee?")

    milk = input("Add extra milk? yes/no: ")

    sugar = input("Add sugar? yes/no: ")

    if milk.lower() == "yes":
        print("Extra milk added")

    if sugar.lower() == "yes":
        print("Sugar added")

    if milk.lower() != "yes" and sugar.lower() != "yes":
        print("No customisation selected")


def calculate_total(price, quantity):

    total = price * quantity

    return total


def payment(total):

    print(f"\nYour total is £{total:.2f}")

    while True:

        amount = float(input("Enter payment amount: £"))

        if amount >= total:

            change = amount - total

            print(f"Payment successful!")
            print(f"Your change is £{change:.2f}")

            return amount, change

        else:

            print("Insufficient payment.")
            print(f"You need £{total - amount:.2f} more.")


def receipt(coffee_name, price, quantity, total, amount, change):

    print("\n==============================")
    print("          RECEIPT")
    print("==============================")

    print(f"Coffee       : {coffee_name}")
    print(f"Price        : £{price:.2f}")
    print(f"Quantity     : {quantity}")
    print(f"Total        : £{total:.2f}")
    print(f"Paid         : £{amount:.2f}")
    print(f"Change       : £{change:.2f}")

    print("==============================")
    print("Thank you for visiting Costa!")
    print("==============================")


def menu():

    while True:

        # 1. Home
        home()

        # 2. Select coffee
        coffee_name = select_coffee()

        if coffee_name is None:
            continue

        # 3. Get quantity
        quantity_value = quantity()

        # 4. Get price
        price = get_price(coffee_name)

        print(f"\n{coffee_name} costs £{price:.2f}")

        # 5. Customise
        customise_coffee()

        # 6. Calculate total
        total = calculate_total(price, quantity_value)

        # 7. Payment
        amount, change = payment(total)

        # 8. Receipt
        receipt(
            coffee_name,
            price,
            quantity_value,
            total,
            amount,
            change
        )

        # 9. Another order?
        again = input("\nPress 'start' to order again or 'exit' to leave: ")

        if again.lower() == "start":

            print("\nStarting a new order...")

        else:

            print("\nThank you! Have a great day.")
            break


menu()