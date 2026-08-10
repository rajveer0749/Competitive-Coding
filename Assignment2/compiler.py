class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def hasCycle(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False

n = int(input("Enter number of nodes: "))
values = list(map(int, input("Enter values: ").split()))
pos = int(input("Enter pos (-1 for no cycle): "))

nodes = [ListNode(value) for value in values]

for i in range(n - 1):
    nodes[i].next = nodes[i + 1]

if pos != -1:
    nodes[-1].next = nodes[pos]

head = nodes[0] if n > 0 else None

print(hasCycle(head))