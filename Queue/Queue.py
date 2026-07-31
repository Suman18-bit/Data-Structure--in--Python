class Queue:
    def __init__(self):
        self.queue = []

    # Enqueue operation
    def enqueue(self, item):
        self.queue.append(item)
        print(f"Enqueued {item}")

    # Dequeue operation
    def dequeue(self):
        if self.isEmpty():
            print("Queue Underflow")
            return None
        return self.queue.pop(0)

    # Peek operation
    def peek(self):
        if self.isEmpty():
            print("Queue is empty")
            return None
        return self.queue[0]

    # Check if empty
    def isEmpty(self):
        return len(self.queue) == 0

    # Size of queue
    def size(self):
        return len(self.queue)

    # Print queue
    def printQueue(self):
        print("Queue:", self.queue)


# Driver code
if __name__ == "__main__":
    q = Queue()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)

    q.printQueue()   # Output: Queue: [10, 20, 30]

    print("Front element:", q.peek())  # Output: 10

    q.dequeue()
    q.printQueue()   # Output: Queue: [20, 30]
