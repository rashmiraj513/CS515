from Node import DoublyLL as Node

class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def insertAtBegin(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            return
    
    def insertAtIndex(self, value, index):
        new_node = Node(value)
        position = 0
        if index == 0:
            self.insertAtBegin(value)
            return
        else:
            curr = self.head
            while curr != None and position + 1 != index:
                position += 1
                curr = curr.next
            if curr is not None:
                new_node.next = curr.next
                curr.next.prev = new_node
                curr.next = new_node
                new_node.prev = curr
                return
            else:
                print('Index out of range!')
                return

    def insertAtEnd(self, value):
        new_node = Node(value)
        if self.head is None:
            self.insertAtBegin(value)
            return
        else:
            curr = self.head
            while curr.next != None:
                curr = curr.next
            curr.next = new_node
            new_node.prev = curr
            return  
    
    def display(self):
        curr = self.head
        print('The Linked List elements are: ', end="")
        while curr is not None:
            print(curr.data, end=" -> ")
            curr = curr.next
        print('NULL')

    def length(self):
        count = 0
        curr = self.head
        while curr is not None:
            count += 1
            curr = curr.next
        return count
    
    def search(self, value):
        curr = self.head
        index = 0
        while curr is not None:
            if curr.data == value:
                return index
            curr = curr.next
            index += 1
        return -1
    
    def deleteFromBegin(self):
        if self.head is not None:
            val = self.head.data
            self.head.next.prev = None
            self.head = self.head.next
            return val
        else:
            print('Linked List is empty!')
            return None
        
    def deleteFromIndex(self, index):
        position = 0
        if index == 0:
            self.deleteFromBegin()
            return
        else:
            curr = self.head
            while curr != None and position + 1 != index:
                position += 1
                curr = curr.next
            if curr is not None:
                val = curr.next.data
                curr.next = curr.next.next
                curr.next.prev = curr
                return val
            else:
                print('Index out of range!')
                return None
    
    def deleteFromEnd(self):    
        if self.head is not None:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            val = curr.data
            curr.next.prev = None
            curr.next = None
            return val
        else:
            print('Linked List is empty')
            return None
    
    def deleteByValue(self, value):
        if self.head is not None:
            curr = self.head
            while curr.next != None:
                if curr.data == value:
                    val = curr.data
                    curr.data = curr.next.data
                    curr.next = curr.next.next
                    return val
                curr = curr.next
            # For last node
            if curr.data == value:
                val = curr.data
                curr.data = curr.next.data
                curr.next = curr.next.next
                return val
            else:
                print('Value not found!')
                return None
        else:
            print('Linked List is empty!')
            return None
    
# Driver Code
if __name__ == "__main__":
    str = '''
    Doubly linked lists offer advantages over singly linked lists like:

    1. Bidirectional Traversal:
    - Doubly linked lists allow both forward and backward traversal, as each node contains pointers to both its next and previous nodes.

    2. Insertion and Deletion Efficiency:
    - Insertion and deletion operations at any position in a doubly linked list are more efficient compared to singly linked lists, as there is no need to traverse the list from the beginning to update adjacent pointers.

    3. Easier Removal of Nodes:
    - Deleting a node in a doubly linked list is more straightforward as it requires adjusting the pointers of the preceding and succeeding nodes, unlike singly linked lists where you need to traverse from the head to update the previous node's pointer.

    4. Reverse Traversal:
    - Doubly linked lists enable easy reverse traversal, which is beneficial in scenarios where operations need to be performed from the end of the list.

    '''
    print(str)
    doublyLinkedList = DoublyLinkedList()
    doublyLinkedList.insertAtBegin(1)
    doublyLinkedList.insertAtBegin(2)
    doublyLinkedList.display()
    doublyLinkedList.insertAtEnd(3)
    doublyLinkedList.insertAtEnd(4)
    doublyLinkedList.display()
    doublyLinkedList.insertAtIndex(12, 3)
    doublyLinkedList.display()
    doublyLinkedList.deleteByValue(2)
    doublyLinkedList.display()