from collections import deque

class Stack:

    def __init__(self) -> None:
        self.stack = deque()

    def __str__(self) -> str:
        return f"Stack{self.stack}".replace("deque","")

    def push(self, element) -> None:
        """
        Inserts an element onto the stack
        """
        self.stack.append(element)

    def pop(self):
        """
        Removes the last element from the list and returns the same
        """
        if self.size():
            return self.stack.pop()
        
    def size(self) -> int:
        return len(self.stack)
        
    def peek(self):
        """
        Returns the last element of the stack without removing the same
        """
        if self.size():
            return self.stack[-1]
        
    def is_empty(self):
        return self.size() == 0
    
    def search(self, element) -> list:
        """
        Returns the indices where the element is found
        """
        return [i for i in range(self.size()) if self.stack[i] == element]

if __name__ == "__main__":
    stack = Stack()
    print(stack.size)
    elements = [5,9,1,7,3,9,1]
    print(stack.peek())

    for element in elements:
        print(f"Element {element} is pushed onto the stack")
        stack.push(element)
    
        print(stack)
    print(stack.size())
    print(f"1 is present in indices => {stack.search(1)}")

    for _ in range(3):
        print(f"last element popped => {stack.pop()}")

    print(stack)
    print(stack.peek())
    print(stack.size())
    print(stack)
