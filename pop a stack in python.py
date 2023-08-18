class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return "Stack is empty"

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return "Stack is empty"


# Creating a stack
stack = Stack()

# Pushing elements onto the stack
stack.push(11)
stack.push(34)
stack.push(57)

# Popping elements from the stack
popped_item = stack.pop()
print("Popped:", popped_item)

# Peeking at the top element
top_element = stack.peek()
print("Top element:", top_element)
