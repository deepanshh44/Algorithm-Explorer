def get_complexity(algorithm):
    if algorithm == "linear_search":
        return {
            "name": "Linear Search",
            "best": "O(1)",
            "worst": "O(n)",
            "space": "O(1)",
            "explanation": "The elements are checked one by one until the target is found or the list ends."
        }

    elif algorithm == "selection_sort":
        return {
            "name": "Selection Sort",
            "best": "O(n²)",
            "worst": "O(n²)",
            "space": "O(1)",
            "explanation": "The algorithm repeatedly finds the smallest element from the unsorted part."
        }

    elif algorithm == "factorial":
        return {
            "name": "Factorial (Recursive)",
            "best": "O(n)",
            "worst": "O(n)",
            "space": "O(n)",
            "explanation": "The function repeatedly calls itself with n-1 until the base condition is reached."
        }

    elif algorithm == "fibonacci":
        return {
            "name": "Fibonacci (Recursive)",
            "best": "O(2^n)",
            "worst": "O(2^n)",
            "space": "O(n)",
            "explanation": "Each recursive call creates additional recursive calls until the base conditions are reached."
        }

    elif algorithm == "tower_of_hanoi":
        return {
            "name": "Tower of Hanoi",
            "best": "O(2^n)",
            "worst": "O(2^n)",
            "space": "O(n)",
            "explanation": "The recursive solution generates a growing number of moves as the number of disks increases."
        }

    else:
        return None
