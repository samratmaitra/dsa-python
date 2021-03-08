class BinarySearchTreeNode:

    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

    def __str__(self) -> str:
        return f"BinarySearchTree({self.in_order_traversal()})"

    def add_child(self, data) -> None:
        if data == self.data:
            return
        elif data < self.data:
            # add node in left sub tree
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            # add node in right sub tree
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)
    
    def in_order_traversal(self) -> list:
        elements = []
        # visit left sub tree
        if self.left:
            elements += self.left.in_order_traversal()
        # visit root
        elements.append(self.data)
        # visit right sub tree
        if self.right:
            elements += self.right.in_order_traversal()
        return elements
    
    def pre_order_traversal(self) -> list:
        elements = []
        # visit root
        elements.append(self.data)
        # visit left sub tree
        if self.left:
            elements += self.left.pre_order_traversal()
        # visit right sub tree
        if self.right:
            elements += self.right.pre_order_traversal()
        return elements
    
    def post_order_traversal(self) -> list:
        elements = []
        # visit left sub tree
        if self.left:
            elements += self.left.post_order_traversal()
        # visit right sub tree
        if self.right:
            elements += self.right.post_order_traversal()
        # visit root
        elements.append(self.data)
        return elements
    
    def seach(self, data) -> bool:
        if data == self.data:
            return True
        elif data < self.data:
            # data may be in left sub tree
            if self.left:
                return self.left.seach(data)
            else:
                return False
        else:
            # data may be in right sub tree
            if self.right:
                return self.right.seach(data)
            else:
                return False
            
    def min(self):
        return self.in_order_traversal()[0]
    
    def max(self):
        return self.in_order_traversal()[-1]
    
    def sum(self):
        return sum(self.in_order_traversal())
    
    def delete(self, data):
        if not self.seach(data):
            # Return None if the data to be deleted does not exist in the BST
            return
        if data < self.data:
            # data to be deleted is smaller than the current node
            # delete from left tree
            self.left = self.left.delete(data)
        elif data > self.data:
            # data to be deleted is bigger than the current node
            # delete from right tree
            self.right = self.right.delete(data)
        else:
            # found the node to be deleted
            # case 1: delete leaf node
            if not self.left and not self.right:
                return
            # case 2: delete node w/ 1 child
            if not self.left:
                return self.right
            if not self.right:
                return self.left
            # case 3: delete node w/ 2 children
            if self.left and self.right:
                min_val = self.right.min()
                self.data = min_val
                self.right = self.right.delete(min_val)
        return self
            
if __name__ == "__main__":
    elements = [7,3,8,2,1,9]
    root = BinarySearchTreeNode(elements[0])
    for element in elements[1:]:
        root.add_child(element)
    print(root)
    root.delete(7)
    print(root)
