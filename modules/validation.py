def get_integer(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter an integer.")


def get_number_list(prompt):
    while True:
        user_input = input(prompt).strip()

        if not user_input:
            print("Input cannot be empty.")
            continue

        try:
            numbers = [int(number) for number in user_input.split()]
            return numbers
        except ValueError:
            print("Invalid input. Please enter numbers separated by spaces.")


def get_positive_integer(prompt):
    while True:
        value = get_integer(prompt)

        if value > 0:
            return value

        print("Please enter a value greater than 0.")


def get_non_negative_integer(prompt):
    while True:
        value = get_integer(prompt)

        if value >= 0:
            return value

        print("Please enter a non-negative integer.")
       
