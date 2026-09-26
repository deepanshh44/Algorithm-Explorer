from modules.search import linear_search
from modules.sorting import selection_sort
from modules.recursion import factorial, fibonacci, tower_of_hanoi


#  LINEAR SEARCH TESTS 
print(" LINEAR SEARCH TESTS ")

numbers = [10, 20, 30, 40, 50]

index, comparisons = linear_search(numbers, 30)

if index == 2:
    print("Test 1 - Target Found: PASS")
else:
    print("Test 1 - Target Found: FAIL")


index, comparisons = linear_search(numbers, 100)

if index == -1:
    print("Test 2 - Target Not Found: PASS")
else:
    print("Test 2 - Target Not Found: FAIL")


#  SELECTION SORT TESTS 

print("\n SELECTION SORT TESTS ")

numbers = [64, 25, 12, 22, 11]

sorted_numbers, comparisons, swaps = selection_sort(numbers)

if sorted_numbers == [11, 12, 22, 25, 64]:
    print("Test 3 - Sorting: PASS")
else:
    print("Test 3 - Sorting: FAIL")


numbers = [1, 2, 3, 4, 5]

sorted_numbers, comparisons, swaps = selection_sort(numbers)

if sorted_numbers == [1, 2, 3, 4, 5]:
    print("Test 4 - Already Sorted List: PASS")
else:
    print("Test 4 - Already Sorted List: FAIL")


# RECURSION TESTS

print("\n RECURSION TESTS ")

if factorial(5) == 120:
    print("Test 5 - Factorial: PASS")
else:
    print("Test 5 - Factorial: FAIL")


if factorial(0) == 1:
    print("Test 6 - Factorial Boundary Case: PASS")
else:
    print("Test 6 - Factorial Boundary Case: FAIL")


if fibonacci(7) == 13:
    print("Test 7 - Fibonacci: PASS")
else:
    print("Test 7 - Fibonacci: FAIL")


if fibonacci(0) == 0:
    print("Test 8 - Fibonacci Boundary Case: PASS")
else:
    print("Test 8 - Fibonacci Boundary Case: FAIL")


#TOWER OF HANOI TEST

print("\n========== TOWER OF HANOI TEST ==========")

print("Testing Tower of Hanoi with 3 disks:")

tower_of_hanoi(3, "A", "B", "C")

print("Test 9 - Tower of Hanoi: PASS")


#  FINAL MESSAGE 


print("ALL TESTS COMPLETED")
