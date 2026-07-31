class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]  # list of lists

    # Hash function
    def _hash(self, key):
        return hash(key) % self.size

    # Insert key-value pair
    def insert(self, key, value):
        index = self._hash(key)
        # Check if key already exists → update
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        # Otherwise, add new pair
        self.table[index].append([key, value])

    # Search by key
    def search(self, key):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None

    # Delete by key
    def delete(self, key):
        index = self._hash(key)
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                del self.table[index][i]
                return True
        return False

    # Display table
    def display(self):
        for i, bucket in enumerate(self.table):
            print(f"Index {i}: {bucket}")


# Driver code
if __name__ == "__main__":
    ht = HashTable(5)

    ht.insert("name", "SUMAN")
    ht.insert("age", 21)
    ht.insert("city", "Nandigram")

    ht.display()
    print("Search 'city':", ht.search("city"))

    ht.delete("age")
    ht.display()
