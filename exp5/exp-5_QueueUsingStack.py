class Queue:

    def __init__(self):
        self.inputStack = []
        self.outputStack = []

    def enqueue(self, element):
        self.inputStack.append(element)
        print(element, "added to queue")

    def dequeue(self):
        if not self.outputStack:
            while self.inputStack:
                self.outputStack.append(self.inputStack.pop())

        if not self.outputStack:
            return "Queue is Empty"

        return self.outputStack.pop()

    def front(self):
        if not self.outputStack:
            while self.inputStack:
                self.outputStack.append(self.inputStack.pop())

        if not self.outputStack:
            return "Queue is Empty"

        return self.outputStack[-1]

    def isEmpty(self):
        return len(self.inputStack) == 0 and len(self.outputStack) == 0


queue = Queue()

while True:
    print("\nQueue Menu")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Front")
    print("4. Check if Empty")
    print("5. Exit")

    option = int(input("Enter your choice: "))

    if option == 1:
        value = int(input("Enter value to enqueue: "))
        queue.enqueue(value)

    elif option == 2:
        print("Removed:", queue.dequeue())

    elif option == 3:
        print("Front:", queue.front())

    elif option == 4:
        if queue.isEmpty():
            print("Queue is Empty")
        else:
            print("Queue is Not Empty")

    elif option == 5:
        print("Exiting")
        break

    else:
        print("Invalid Choice")