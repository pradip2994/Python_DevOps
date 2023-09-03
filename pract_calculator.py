## Python if...elif...else Statement
## Creating a Calculator

# while True: and try: combination is commonly used in scenarios where we want to repeatedly execute code until a certain condition is met, and need to handle potential exceptions that may occur during the execution of that code.

while True:
    try:
        num_1 = float(input("Enter the first number: "))
        num_2 = float(input("Enter the second number: " ))
        choice = input("enter the the operations like: +, -, *, /, % :" )

        if choice == "+":
            sum = num_1 + num_2
            print("Addition of two number is :", sum)

        elif choice == "-":
            diff = num_1 - num_2
            print("Subtraction of two number is: ", diff)

        elif choice == "*":
            multi = num_1 * num_2
            print("Multiplication of two numbers is: ", multi)

        elif choice == "/":
            if num_2 == 0:
                print("Division with 0 not allowed")
            else:
                div = num_1 / num_2
                print("Division of two numbers is :", div)

        elif choice == "%":
            per = num_1 % num_2
            print("Remainder (Modulus) is: ", per)

        else:
            print("Invalid input choice")

# except ValueError: allows to handle different types of exceptions in different ways, tailoring error messages and actions to the specific error conditions that may arise in code.

    except ValueError:
        print("Invalid input.")

# ask_user.lower(): This part converts the user's input to lowercase, ensuring that the comparison is not case-sensitive.
# !=: This is "not equal to."

    ask_user = input("Do you want to perform another calculation? (yes/no): ")
    if ask_user.lower() != "yes":
        break