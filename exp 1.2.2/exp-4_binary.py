numbers = []

print("Enter array size:")
size = int(input())

print("Enter array elements (in sorted order):")
for i in range(size):
    numbers.append(int(input()))

target = int(input("Enter element to search: "))

left = 0
right = size - 1
position = -1

while left <= right:
    middle = (left + right) // 2

    if numbers[middle] == target:
        position = middle
        break
    elif numbers[middle] < target:
        left = middle + 1
    else:
        right = middle - 1

if position != -1:
    print("Element found at index", position)
else:
    print(position)