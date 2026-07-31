# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None

    # Insert at end
    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    # Delete by value
    def delete(self, key):
        temp = self.head

        # If head node itself holds the key
        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            return

        # Search for the key
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        # If key not found
        if temp is None:
            return

        # Unlink the node
        prev.next = temp.next
        temp = None

    # Print list
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

# Driver code
if __name__ == "__main__":
    llist = LinkedList()
    llist.insert(10)
    llist.insert(20)
    llist.insert(30)

    llist.print_list()   # Output: 10 -> 20 -> 30 -> None

    llist.delete(20)
    llist.print_list()   # Output: 10 -> 30 -> None
