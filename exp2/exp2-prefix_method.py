numbers = []

print("Enter the number of elements:")
size = int(input())

result = [1] * size

print("Enter the elements:")
for index in range(size):
    numbers.append(int(input()))

left_product = [1]

for index in range(1, size):
    left_product.append(left_product[index - 1] * numbers[index - 1])

right_product = [1] * size

for index in range(size - 2, -1, -1):
    right_product[index] = right_product[index + 1] * numbers[index + 1]

for index in range(size):
    result[index] = left_product[index] * right_product[index]

print(result)