class Queue:
    def __init__(self):
        self.items = []
    
    # Function to push an item into the queue.
    def enqueue(self, item):
        self.items.append(item)

    # Function to pop an element from the queue.
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("Queue is empty!\n")

    # Function to check whether the queue is empty or not.
    def is_empty(self):
        # Checks if the queue is empty.
        return len(self.items) == 0

    # Function to return the front element of the Queue
    def front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("Queue is empty!\n")