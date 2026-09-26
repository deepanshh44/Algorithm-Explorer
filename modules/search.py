def linear_search(numbers, target):
    comparisons = 0

    for index in range(len(numbers)):
        comparisons += 1

        if numbers[index] == target:
            return index, comparisons

    return -1, comparisons
if __name__ == "__main__":
    numbers = [10, 25, 7, 42, 19]
    target = 42

    index, comparisons = linear_search(numbers, target)

    if index != -1:
        print("Target found!")
        print("Position:", index + 1)
        print("Comparisons:", comparisons)
    else:
        print("Target not found.")
        print("Comparisons:", comparisons)