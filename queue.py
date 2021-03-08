from collections import deque

class Queue:

    def __init__(self) -> None:
        self.queue = deque()

    def __str__(self) -> str:
        return f"Queue{self.queue}".replace("deque","")
    
    def enque(self, element) -> None:
        self.queue.append(element)

    def deque(self):
        if len(self.queue):
            return self.queue.popleft()
        
    def size(self) -> int:
        return len(self.queue)
    
    def search(self, element) -> list:
        return [i for i in range(self.size()) if self.queue[i] == element]

if __name__ == "__main__":
    q = Queue()
    elements = [5,10,15,12,20,24,28,24]
    for element in elements:
        q.enque(element)
    print(q.search(24))
    print(q)

    for _ in range(2):
        print(q.deque())
        print(q)

    q.enque(15)
    q.enque(20)

    print(q)
