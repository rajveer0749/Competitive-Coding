def check_duplicate(values, limit):
    positions = {}

    for index in range(len(values)):
        if values[index] in positions:
            if index - positions[values[index]] <= limit:
                return True

        positions[values[index]] = index

    return False


numbers = []

count = int(input("Enter the number of elements: "))

print("Enter the elements:")
for position in range(count):
    numbers.append(int(input()))

distance = int(input("Enter k: "))

print(check_duplicate(numbers, distance))