from modules.search import linear_search
from modules.sorting import selection_sort
from modules.recursion import factorial, fibonacci, tower_of_hanoi
from modules.complexity import get_complexity

from modules.validation import (
    get_integer,
    get_number_list,
    get_positive_integer,
    get_non_negative_integer
)

def display_menu():
    print("\n===================================")
    print("       ALGORITHM EXPLORER")
    print("     COMPLEXITY ANALYZER")
    print("===================================")
    print("1. Search Lab")
    print("2. Sorting Lab")
    print("3. Recursion Lab")
    print("4. Complexity Analyzer")
    print("5. Exit")
    print("===================================")


def main():
    while True:
        display_menu()

        choice = input("Select any option: ")

# SEARCH LAB   
        if choice == "1":
            print("\n========== SEARCH LAB ==========")

            numbers = get_number_list(
                "Enter numbers separated by spaces: "
            )

            target = get_integer(
            "Enter the number to search: "
            )

            index, comparisons = linear_search(numbers, target)

            if index != -1:
                print("\nTarget found!")
                print("Position:", index + 1)
                print("Comparisons:", comparisons)
            else:
                print("\nTarget not found.")
                print("Comparisons:", comparisons)

#  SORTING LAB
        elif choice == "2":
            print("\n========== SORTING LAB ==========")

            numbers = get_number_list(
            "Enter numbers separated by spaces: "
            )

            sorted_numbers, comparisons, swaps = selection_sort(numbers)

            print("\nOriginal list:", numbers)
            print("Sorted list:", sorted_numbers)
            print("Comparisons:", comparisons)
            print("Swaps:", swaps)

#  RECURSION LAB 
        elif choice == "3":
            print("\n========== RECURSION LAB ==========")
            print("1. Factorial")
            print("2. Fibonacci")
            print("3. Tower of Hanoi")
            print("4. Back to Main Menu")

            recursion_choice = input("Enter your choice: ")

            if recursion_choice == "1":
                n = get_non_negative_integer(
                "Enter a non-negative integer: "
                )

                result = factorial(n)
                print("Factorial of", n, "=", result)
                if n < 0:
                    print("Please enter a non-negative integer.")
                else:
                    result = factorial(n)
                    print("Factorial of", n, "=", result)

            elif recursion_choice == "2":
                n = get_non_negative_integer(
                    "Enter a non-negative integer: "
                )
                
                result = fibonacci(n)
                print("Fibonacci term", n, "=", result)

            elif recursion_choice == "3":
                n = get_positive_integer(
                    "Enter number of disks: "
                )

                print("\nTower of Hanoi moves:")
                tower_of_hanoi(n, "A", "B", "C")   

            elif recursion_choice == "4":
                print("Returning to main menu.")

            else:
                print("Invalid choice.")

#  COMPLEXITY ANALYZER 
       
        elif choice == "4":
            print("\n========== COMPLEXITY ANALYZER ==========")
            print("1. Linear Search")
            print("2. Selection Sort")
            print("3. Factorial")
            print("4. Fibonacci")
            print("5. Tower of Hanoi")
            print("6. Back to Main Menu")

            complexity_choice = input("Enter your choice: ")

            if complexity_choice == "1":
                result = get_complexity("linear_search")

            elif complexity_choice == "2":
                result = get_complexity("selection_sort")

            elif complexity_choice == "3":  
                result = get_complexity("factorial")

            elif complexity_choice == "4":
                result = get_complexity("fibonacci")

            elif complexity_choice == "5":
                result = get_complexity("tower_of_hanoi")

            elif complexity_choice == "6":
                print("Returning to main menu.")
                continue

            else:
                print("Invalid choice.")
                continue

            print("\nAlgorithm:", result["name"])
            print("Best Case:", result["best"])
            print("Worst Case:", result["worst"])
            print("Space Complexity:", result["space"])
            print("Explanation:", result["explanation"])
#  EXIT 
        elif choice == "5":
            print("\nIam Algorithm Explorer!!")
            break

        else:
            print("\nInvalid choice. Please select a number from 1 to 5.")


if __name__ == "__main__":
    main()