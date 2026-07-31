class Stack:
    def __init__(self):
        self.stack = []  # using Python list

    # Push operation
    def push(self, item):
        self.stack.append(item)
        print(f"Pushed {item}")

    # Pop operation
    def pop(self):
        if self.isEmpty():
            print("Stack Underflow")
            return None
        return self.stack.pop()

    # Peek operation
    def peek(self):
        if self.isEmpty():
            print("Stack is empty")
            return None
        return self.stack[-1]

    # Check if empty
    def isEmpty(self):
        return len(self.stack) == 0

    # Size of stack
    def size(self):
        return len(self.stack)

    # Print stack
    def printStack(self):
        print("Stack:", self.stack)


# Driver code
if __name__ == "__main__":
    s = Stack()
    s.push(10)
    s.push(20)
    s.push(30)

    s.printStack()   # Output: Stack: [10, 20, 30]

    print("Top element:", s.peek())  # Output: 30

    s.pop()
    s.printStack()   # Output: Stack: [10, 20]
