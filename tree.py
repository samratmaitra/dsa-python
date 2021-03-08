class TreeNode:

    def __init__(self, data) -> None:
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child) -> None:
        child.parent = self
        self.children.append(child)

    def get_level(self) -> int:
        level = 0
        itr = self
        while itr.parent:
            itr = itr.parent
            level += 1
        return level

    def __str__(self) -> str:
        o_str = str(self.data)
        for child in self.children:
            level = child.get_level()
            o_str += "\n" + level*"\t" + "|__" + str(child)
        return o_str
    
if __name__ == "__main__":
    root = TreeNode("Electronics")

    r1 = TreeNode("Laptop")
    r2 = TreeNode("Mobile Phone")

    r3 = TreeNode("iPhone")
    r4 = TreeNode("htc")

    r5 = TreeNode("MacBook")
    r6 = TreeNode("hp")

    r1.add_child(r5)
    r1.add_child(r6)

    r2.add_child(r3)
    r2.add_child(r4)

    root.add_child(r1)
    root.add_child(r2)

    # print(root, root.get_level())
    # print(r1, r1.get_level())
    # print(r2, r2.get_level())
    # print(r3, r3.get_level())
    # print(r4, r4.get_level())
    # print(r5, r5.get_level())
    # print(r6, r6.get_level())
    print(root)