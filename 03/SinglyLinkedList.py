from Node import SinglyLL as Node

class SinglyLinkedList:
    def __init__(self):
        self.head = None
    
    def insertAtBegin(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
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
                curr.next = new_node
                return
            else:
                print('Index out of range!')
    
    def insertAtEnd(self, value):
        new_node = Node(value)
        if self.head is None:
            self.insertAtBegin(value)
            return
        else:
            curr = self.head
            while curr.next!= None:
                curr = curr.next
            curr.next = new_node
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

    def deleteFromBegin(self):
        if self.head is not None:
            val = self.head.data
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
                return val
            else:
                print('Index out of range!')
                return None
            
    def deleteFromEnd(self):
        if self.head is not None:
            curr = self.head
            while curr.next!= None:
                curr = curr.next
            val = curr.data
            curr.next = None
            return val
        else:
            print('Linked List is empty!')
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
            if curr.data == value:
                val = curr.data
                curr.next = None
                return val
            else:
                print('Value not found!')
                return None
        else:
            print('Linked List is empty!')
            return None
        
    def search(self, value):
        curr = self.head
        index = 0
        while curr is not None:
            if curr.data == value:
                return index
            curr = curr.next
            index += 1
        return -1
    
    # Problem e - Iterative Approach for reverse
    def reverseIterative(self):
        prev = None
        curr = self.head
        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev

    # Problem e - Recursive Approach for reverse
    def reverseRecursive(self, head):
        if head is None or head.next is None:
            return head
        newHead = self.reverseRecursive(head.next)
        head.next.next = head
        head.next = None
        return newHead
    
    # Problem d - Function to detect if a linked list has a cycle, if so,
    # determine the length of the cycle.
    def hasCycle(self):
        if self.head is None:
            # returning -1 denotes that there is no cycle or, the Linked list is empty.
            return -1
        slow = fast = self.head
        flag = 0
        while fast != None and fast.next != None and fast.next.next != None:
            if slow == fast and flag != 0:
                count = 1
                slow = slow.next
                while(slow != fast):
                    slow = slow.next
                    count += 1
                return count
 
            slow = slow.next
            fast = fast.next.next
            flag = 1
        return -1  

def reverseRecursiveHelper(curr):
    if curr is None:
        return curr
    elif curr.next is None:
        return curr
    if curr is not None:
        reverseRecursiveHelper(curr.next)
        curr.next.next = curr
        curr.next = None
        return curr
    else:
        print('Linked List is empty!')
        return None

# Driver Code
if __name__ == "__main__":
    singlyLinkedList = SinglyLinkedList()
    singlyLinkedList.insertAtBegin(1)
    singlyLinkedList.insertAtBegin(2)
    singlyLinkedList.display()
    singlyLinkedList.insertAtEnd(3)
    singlyLinkedList.insertAtEnd(4)
    singlyLinkedList.display()
    singlyLinkedList.insertAtIndex(12, 3)
    singlyLinkedList.display()
    singlyLinkedList.reverseIterative()
    singlyLinkedList.head = singlyLinkedList.reverseRecursive(singlyLinkedList.head)
    singlyLinkedList.display()
    print(singlyLinkedList.deleteFromIndex(3))
    singlyLinkedList.deleteByValue(2)
    singlyLinkedList.display()