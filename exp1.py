numbers = []

size = int(input("Enter the number of elements: "))

for index in range(size):
    numbers.append(int(input(f"Enter element {index + 1}: ")))

for first in range(size):
    for second in range(first + 1, size):
        if numbers[first] == numbers[second]:
            print("TRUE")
            break
    else:
        continue
    break
else:
    print("FALSE")