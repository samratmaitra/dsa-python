class BSTNode:

    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data) -> None:
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BSTNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = self.right = BSTNode(data)
    
    def sort(self):
        sorted_elements = []
        if self.left:
            sorted_elements += self.left.sort()
        sorted_elements.append(self.data)
        if self.right:
            sorted_elements += self.right.sort()
        return sorted_elements

if __name__ == "__main__":
    elements = [23,12,87,98,28,28,-15,17,-17,91]
    bst = BSTNode(elements[0])
    for element in elements[1:]:
        bst.add_child(element)
    sorted_elements = bst.sort()
    print(sorted_elements)
