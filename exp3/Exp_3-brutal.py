numbers = []

print("Enter array size:")
size = int(input())

print("Enter array elements:")
for index in range(size):
    numbers.append(int(input()))

value = int(input("Enter new element: "))

position = 0

for index in range(size):
    if numbers[index] == value:
        print("Element found at index:", index)
        break

    elif value > numbers[index]:
        position = index + 1

    else:
        position = index
        break
else:
    print("Element not found, inserting at index:", position)