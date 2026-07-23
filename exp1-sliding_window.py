def check_duplicate(numbers, distance):
    unique_values = set()

    for index in range(len(numbers)):
        if numbers[index] in unique_values:
            return True

        unique_values.add(numbers[index])

        if len(unique_values) > distance:
            unique_values.remove(numbers[index - distance])

    return False


size = int(input("Enter size of array: "))

values = []

for position in range(size):
    value = int(input("Enter element: "))
    values.append(value)

limit = 3

print(check_duplicate(values, limit))