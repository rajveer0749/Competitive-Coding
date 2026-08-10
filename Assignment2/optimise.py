class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None


def hasCycle(head):
    seen = set()

    while head:
        if head in seen:
            return True

        seen.add(head)
        head = head.next

    return False


values = list(map(int, input("Enter values: ").split()))
pos = int(input("Enter cycle position (-1 for no cycle): "))

if not values:
    print(False)
else:
    nodes = [ListNode(x) for x in values]

    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]

    if pos != -1 and 0 <= pos < len(nodes):
        nodes[-1].next = nodes[pos]

    print(hasCycle(nodes[0]))