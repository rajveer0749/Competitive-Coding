class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


def checkCycle(start):
    seen = set()
    pointer = start

    while pointer:
        if pointer in seen:
            return True
        seen.add(pointer)
        pointer = pointer.next

    return False


count = int(input("Enter number of nodes: "))
nodeList = []

for index in range(count):
    value = int(input(f"Enter value of node {index + 1}: "))
    nodeList.append(Node(value))


for index in range(count - 1):
    nodeList[index].next = nodeList[index + 1]


startNode = nodeList[0]

cyclePosition = int(input("Cycle position: "))

if cyclePosition != -1:
    nodeList[-1].next = nodeList[cyclePosition]


if checkCycle(startNode):
    print("Cycle detected")
else:
    print("No cycle detected")