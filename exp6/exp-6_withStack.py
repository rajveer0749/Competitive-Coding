def largest_rectangle(heightList):

    heightList.append(0)

    indexStack = []
    largestArea = 0

    for currentIndex in range(len(heightList)):

        while len(indexStack) > 0 and heightList[currentIndex] < heightList[indexStack[-1]]:

            topIndex = indexStack.pop()

            currentHeight = heightList[topIndex]

            if len(indexStack) == 0:
                currentWidth = currentIndex
            else:
                currentWidth = currentIndex - indexStack[-1] - 1

            currentArea = currentHeight * currentWidth

            if currentArea > largestArea:
                largestArea = currentArea

        indexStack.append(currentIndex)

    heightList.pop()

    return largestArea


print("Enter number of bars:")
size = int(input())

heightList = []

print("Enter the heights:")
for index in range(size):
    height = int(input())
    heightList.append(height)

answer = largest_rectangle(heightList)

print("Largest Rectangle =", answer)