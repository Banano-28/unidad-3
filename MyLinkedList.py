class Node:
    def __init__(self, data):
        self.data = data        
        self.next = None        


class LinkedList:
    def __init__(self):
        self.head = None  

    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def delete(self, data):
        current = self.head
        previous = None

        while current and current.data != data:
            previous = current
            current = current.next

        if current is None:
            print("Elemento no encontrado.")
            return

        if previous is None:
            self.head = current.next
        else:
            previous.next = current.next

    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False
