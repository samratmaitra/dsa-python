class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

    def __str__(self) -> str:
        return str(self.data)
    
class LinkedList:

    def __init__(self, elements:list=None) -> None:
        self.head = None
        self.len = 0
        if elements:
            for element in elements:
                self.append(element)

    def __str__(self) -> str:
        return f"LinkedList({self.get_elements()})"
        
    def __add__(self, ll):
        return LinkedList(self.get_elements()+ll.get_elements())
    
    def get_elements(self) -> list:
        elements = []
        itr = self.head
        while itr:
            elements.append(itr.data)
            itr = itr.next
        return elements

    def append(self, data) -> None:
        node_to_insert = Node(data)
        if self.len == 0:
            self.head = node_to_insert
        else:
            itr = self.head
            while itr.next:
                itr = itr.next
            itr.next = node_to_insert
        self.len += 1

    def prepend(self, data) -> None:
        if self.len == 0:
            self.append(data)
        else:
            node_to_insert = Node(data)
            tmp_node = self.head
            node_to_insert.next = tmp_node
            self.head = node_to_insert
            self.len += 1

    def insert_at(self, pos:int, data) -> None:
        if pos < 0 or pos > self.len:
            raise Exception(f"Error - Index {pos} out of range")
        if pos == 0:
            self.prepend(data)
            return

        ctr = 0
        itr = self.head
        
        while ctr < pos-1:
            itr = itr.next
            ctr += 1

        node_to_insert = Node(data)
        tmp_node = itr.next
        node_to_insert.next = tmp_node
        itr.next = node_to_insert
        self.len += 1

    def remove_at(self, pos:int) -> None:
        if pos < 0 or pos > self.len or self.len == 0:
            raise Exception(f"Error - Index {pos} out of range")
        
        ctr = 0
        itr = self.head

        if pos == 0:
            self.head = self.head.next
            self.len -= 1
            return

        while ctr < pos-1:
            ctr += 1
            itr = itr.next

        node_to_remove = itr.next
        itr.next = node_to_remove.next
        self.len -= 1

    def reverse(self):
        elements = []
        itr = self.head
        while itr:
            elements.append(itr.data)
            itr = itr.next
        elements = elements[::-1]
        return LinkedList(elements)

if __name__ == "__main__":
    ll1 = LinkedList([1,2,3,4])
    ll2 = LinkedList([5,6,7,8])
    ll3 = ll1 + ll2
    print(ll3, ll3.len)
