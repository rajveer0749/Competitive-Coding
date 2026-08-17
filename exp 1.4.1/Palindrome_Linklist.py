class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


def checkPalindrome(start):
    left = start
    right = start
    values = []

    while right and right.next:
        values.append(left.data)
        left = left.next
        right = right.next.next

    if right:
        left = left.next

    while left:
        if values.pop() != left.data:
            return False
        left = left.next

    return True


count = int(input("Enter number of nodes: "))

head = None
last = None

for index in range(count):
    value = int(input("Enter node value: "))
    node = Node(value)

    if head is None:
        head = node
        last = node
    else:
        last.next = node
        last = node


if checkPalindrome(head):
    print("Palindrome")
else:
    print("Not Palindrome")