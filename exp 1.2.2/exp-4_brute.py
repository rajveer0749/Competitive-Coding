numbers = []

print("Enter array size:")
size = int(input())

print("Enter array elements:")
for i in range(size):
    numbers.append(int(input()))

target = int(input("Enter element to search: "))

position = -1

for i in range(size):
    if numbers[i] == target:
        position = i
        break

if position != -1:
    print("Element found at index", position)
else:
    print(position)