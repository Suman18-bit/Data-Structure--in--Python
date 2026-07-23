class Stack:
    def __init__(self, capacity):
        self.capacity = capacity      # maximum size of stack
        self.stack = [None] * capacity  # fixed-size array
        self.top = -1                 # index of top element (-1 means empty)

    # Check if stack is empty
    def is_empty(self):
        return self.top == -1

    # Check if stack is full
    def is_full(self):
        return self.top == self.capacity - 1

    # Push an element onto the stack
    def push(self, item):
        if self.is_full():
            raise OverflowError("Stack overflow: cannot push, stack is full")
        self.top += 1
        self.stack[self.top] = item

    # Pop an element from the stack
    def pop(self):
        if self.is_empty():
            raise IndexError("Stack underflow: cannot pop, stack is empty")
        item = self.stack[self.top]
        self.stack[self.top] = None   # optional: clear the slot
        self.top -= 1
        return item

    # Peek at the top element
    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self.stack[self.top]

    # Get current size
    def size(self):
        return self.top + 1

    # Display stack contents
    def display(self):
        print("Stack:", self.stack[:self.top+1])


# Example usage
stack = Stack(5)   # stack with capacity 5
stack.push(10)
stack.push(20)
stack.push(30)
stack.display()       # Stack: [10, 20, 30]
print(stack.pop())    # 30
print(stack.peek())   # 20
print(stack.size())   # 2

