class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


def checkCycle(start):
    slowPtr = start
    fastPtr = start

    while fastPtr and fastPtr.next:
        slowPtr = slowPtr.next
        fastPtr = fastPtr.next.next

        if slowPtr == fastPtr:
            return True

    return False


count = int(input("Enter number of nodes: "))

nodeList = []

for index in range(count):
    value = int(input(f"Enter value of node {index + 1}: "))
    nodeList.append(Node(value))


# Connect nodes
for index in range(count - 1):
    nodeList[index].next = nodeList[index + 1]


startNode = nodeList[0] if count > 0 else None

cyclePos = int(input("Enter cycle position (-1 for no cycle): "))

if cyclePos != -1:
    nodeList[-1].next = nodeList[cyclePos]


if checkCycle(startNode):
    print("Cycle detected")
else:
    print("No cycle detected")