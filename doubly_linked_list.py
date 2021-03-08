from linked_list import Node, LinkedList

class DoublyNode(Node):

    def __init__(self, data) -> None:
        super().__init__(data)
        self.prev = None

class DoublyLinkedList(LinkedList):

    def __init__(self, elements: list = None) -> None:
        super().__init__(elements)

    def __str__(self) -> str:
        return super().__str__().replace("Linked","DoublyLinked")
    
    def prepend(self, data) -> None:
        if self.len == 0:
            self.append(data)
        else:
            node_to_insert = DoublyNode(data)
            tmp_node = self.head
            node_to_insert.prev = self.head
            node_to_insert.next = tmp_node
            self.head = node_to_insert
            self.len += 1    
    
    def append(self, data) -> None:
        node_to_insert = DoublyNode(data)
        if self.len == 0:
            node_to_insert.prev = self.head
            self.head = node_to_insert
        else:
            itr = self.head
            while itr.next:
                itr = itr.next

            node_to_insert.prev = itr.next
            itr.next = node_to_insert
        self.len += 1

    def insert_at(self, pos: int, data) -> None:
        if pos < 0 or pos > self.len:
            raise Exception(f"Error - Index {pos} out of range")
        if pos == 0:
            self.prepend(data)
            return
        
        if pos == self.len:
            self.append(data)
            return

        ctr = 0
        itr = self.head
        
        while ctr < pos-1:
            itr = itr.next
            ctr += 1

        node_to_insert = DoublyNode(data)
        tmp_node = itr.next
        node_to_insert.next = tmp_node
        node_to_insert.prev = itr
        tmp_node.prev = node_to_insert
        itr.next = node_to_insert
        self.len += 1

    def remove_at(self, pos: int) -> None:
        pass

    def reverse(self):
        rev_elements = super().reverse().get_elements()
        return DoublyLinkedList(rev_elements)

if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.prepend(100)
    print(dll)
    dll.append(15)
    dll.append(25)
    print(dll)
    print(dll.reverse())
    dll.prepend(500)
    print(dll)
    dll.insert_at(5,19)
    print(dll)
