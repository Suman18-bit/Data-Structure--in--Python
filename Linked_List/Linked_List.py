// Node class
class Node {
    int data;
    Node next;

    Node(int data) {
        this.data = data;
        this.next = null;
    }
}

// LinkedList class
class LinkedList {
    Node head; // first node

    // Insert at end
    public void insert(int data) {
        Node newNode = new Node(data);

        if (head == null) {
            head = newNode;
            return;
        }

        Node temp = head;
        while (temp.next != null) {
            temp = temp.next;
        }
        temp.next = newNode;
    }

    // Delete by value
    public void delete(int key) {
        Node temp = head, prev = null;

        // If head node itself holds the key
        if (temp != null && temp.data == key) {
            head = temp.next; // change head
            return;
        }

        // Search for the key
        while (temp != null && temp.data != key) {
            prev = temp;
            temp = temp.next;
        }

        // If key not found
        if (temp == null) return;

        // Unlink the node
        prev.next = temp.next;
    }

    // Print list
    public void printList() {
        Node temp = head;
        while (temp != null) {
            System.out.print(temp.data + " -> ");
            temp = temp.next;
        }
        System.out.println("null");
    }
}

// Driver code
public class Main {
    public static void main(String[] args) {
        LinkedList list = new LinkedList();

        list.insert(10);
        list.insert(20);
        list.insert(30);

        list.printList(); // Output: 10 -> 20 -> 30 -> null

        list.delete(20);
        list.printList(); // Output: 10 -> 30 -> null
    }
}
