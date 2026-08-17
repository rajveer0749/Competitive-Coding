result = []
numbers = []

print("Enter array size:")
size = int(input())

print("Enter array elements:")
for index in range(size):
    numbers.append(int(input()))

for index in range(size):
    multiplication = 1

    for position in range(size):
        if index != position:
            multiplication = multiplication * numbers[position]

    result.append(multiplication)

print(result)