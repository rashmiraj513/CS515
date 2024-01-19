class SinglyLL:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class DoublyLL:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next