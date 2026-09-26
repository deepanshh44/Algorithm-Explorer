def selection_sort(numbers):
    numbers = numbers.copy()
    comparisons = 0
    swaps = 0

    for i in range(len(numbers) - 1):
        min_index = i

        for j in range(i + 1, len(numbers)):
            comparisons += 1

            if numbers[j] < numbers[min_index]:
                min_index = j

        if min_index != i:
            numbers[i], numbers[min_index] = numbers[min_index], numbers[i]
            swaps += 1

    return numbers, comparisons, swaps
if __name__ == "__main__":
    numbers = [64, 25, 12, 22, 11]

    sorted_numbers, comparisons, swaps = selection_sort(numbers)

    print("Original list:", numbers)
    print("Sorted list:", sorted_numbers)
    print("Comparisons:", comparisons)
    print("Swaps:", swaps)