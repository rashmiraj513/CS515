from Node import SinglyLL as Node

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        if not self.head:
            print("Circular Linked List is empty.")
            return

        temp = self.head
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print('NULL')

    def insertAtEnd(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    def insertAtBegin(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head
            self.head = new_node

    def insertAtIndex(self, data, index):
        if index < 0:
            print("Invalid index.")
            return

        new_node = Node(data)

        if index == 0:
            self.insertAtBegin(data)
        else:
            count = 0
            temp = self.head
            while count < index - 1 and temp.next != self.head:
                temp = temp.next
                count += 1

            if count == index - 1:
                new_node.next = temp.next
                temp.next = new_node
            else:
                print("Index out of bounds.")

    def deleteFromBegin(self):
        if not self.head:
            print("Circular Linked List is empty.")
            return

        if self.head.next == self.head:
            self.head = None
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = self.head.next
            self.head = self.head.next

    def deleteFromIndex(self, index):
        if not self.head:
            print("Circular Linked List is empty.")
            return

        if index < 0:
            print("Invalid index.")
            return

        if index == 0:
            self.deleteFromBegin()
        else:
            count = 0
            temp = self.head
            prev = None
            while count < index and temp.next != self.head:
                prev = temp
                temp = temp.next
                count += 1

            if count == index:
                prev.next = temp.next
            else:
                print("Index out of bounds.")

    def deleteFromEnd(self):
        if not self.head:
            print("Circular Linked List is empty.")
            return

        if self.head.next == self.head:
            self.head = None
        else:
            temp = self.head
            prev = None
            while temp.next != self.head:
                prev = temp
                temp = temp.next
            prev.next = self.head


# Example usage:
if __name__ == "__main__":
    circularLinkedList = CircularLinkedList()

    circularLinkedList.insertAtEnd(1)
    circularLinkedList.insertAtEnd(2)
    circularLinkedList.insertAtEnd(3)
    circularLinkedList.insertAtEnd(4)

    print("Initial Circular Linked List:")
    circularLinkedList.display()

    circularLinkedList.insertAtBegin(0)
    print("After inserting at the beginning:")
    circularLinkedList.display()

    circularLinkedList.insertAtIndex(2.5, 3)
    print("After inserting at index 3:")
    circularLinkedList.display()

    circularLinkedList.deleteFromBegin()
    print("After deleting from the beginning:")
    circularLinkedList.display()

    circularLinkedList.deleteFromIndex(2)
    print("After deleting at index 2:")
    circularLinkedList.display()

    circularLinkedList.deleteFromEnd()
    print("After deleting from the end:")
    circularLinkedList.display()