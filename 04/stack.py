class Stack:
    def __init__(self):
        self.items = []

    # Function to insert an item onto the stack.
    def push(self, item):
        # Pushes an item onto the stack.
        self.items.append(item)

    # Function to pop an element from the stack
    def pop(self):
        # Pops and returns the top item from the stack.
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("pop from an empty stack")

    # Function to return the top item from the stack
    def peek(self):
        # Returns the top item from the stack without removing it.
        if not self.is_empty():
            return self.items[-1]
        else:
            return IndexError("The stack is empty!")

    # Function to check whether the stack is empty or not
    def is_empty(self):
        # Checks if the stack is empty.
        return len(self.items) == 0