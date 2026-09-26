def factorial(n):
    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)


def fibonacci(n):
    if n == 0:
        return 0

    if n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)


def tower_of_hanoi(n, source, auxiliary, destination):
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return

    tower_of_hanoi(n - 1, source, destination, auxiliary)

    print(f"Move disk {n} from {source} to {destination}")

    tower_of_hanoi(n - 1, auxiliary, source, destination)

if __name__ == "__main__":
    n = 3

    print("Tower of Hanoi:")
    tower_of_hanoi(n, "A", "B", "C")