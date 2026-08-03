from collections import deque

class Stack:
    def __init__(self):
        self.q = deque()

    def push(self, x):
        self.q.append(x)
        print(x, "pushed into stack")

    def pop(self):
        if self.q:
            for i in range(len(self.q) - 1):
                self.q.append(self.q.popleft())
            return self.q.popleft()
        return "Stack is Empty"

    def top(self):
        if self.q:
            return self.q[-1]
        return "Stack is Empty"

    def isEmpty(self):
        return len(self.q) == 0


s = Stack()

while True:
    print("\nStack Menu")
    print("1. Push")
    print("2. Pop")
    print("3. Top")
    print("4. Check if Empty")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        value = int(input("Enter value to push: "))
        s.push(value)

    elif choice == 2:
        print("Removed:", s.pop())

    elif choice == 3:
        print("Top:", s.top())

    elif choice == 4:
        if s.isEmpty():
            print("Stack is Empty")
        else:
            print("Stack is Not Empty")

    elif choice == 5:
        print("Exiting")
        break

    else:
        print("Invalid")