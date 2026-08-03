# Largest Rectangle in Histogram (Brute Force)

def largest_rectangle(heightList):
    largestArea = 0
    size = len(heightList)

    for start in range(size):
        minimumHeight = heightList[start]

        for end in range(start, size):
            minimumHeight = min(minimumHeight, heightList[end])
            currentArea = minimumHeight * (end - start + 1)
            largestArea = max(largestArea, currentArea)

    return largestArea


print("Enter number of values:")
size = int(input())

heightList = []

print("Enter the heights:")
for index in range(size):
    heightList.append(int(input()))

answer = largest_rectangle(heightList)

print("Largest rectangle:", answer)