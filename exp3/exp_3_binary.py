numbers = []

print("Enter array size:")
size = int(input())

print("Enter array elements:")
for i in range(size):
    numbers.append(int(input()))

target = int(input("Enter new element: "))

left = 0
right = size - 1

while left <= right:
    middle = (left + right) // 2

    if numbers[middle] == target:
        print("Element found at index:", middle)
        break

    elif numbers[middle] < target:
        left = middle + 1

    else:
        right = middle - 1

print("Inserting at index:", left)