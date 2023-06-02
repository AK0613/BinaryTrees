#Binary Trees
# Given a tree, find its maximum depth

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

class BinaryTree:
    def __init__(self):
        self.root = None
        self.elements = 0

    def add(self, value):
        node = Node(value)
        # IF empty
        if self.root is None:
            self.root = node
            self.elements += 1

        else:
            # Iterator
            current = self.root

            while (current):
                #Parent will hold the previous node we are visiting.
                parent = current
                if current.data > value:
                    current = current.left

                    if current is None:
                        parent.left = node

                elif current.data < value:
                    current = current.right

                    if current is None:
                        parent.right = node


    def print_in_order(self, node):
        if node:
            self.print_in_order(node.left)
            print(f"{node.data} ")
            self.print_in_order(node.right)

    def print_post_order(self, node):
        if node:
            self.print_post_order(node.left)
            self.print_post_order(node.right)
            print(f"{node.data} ")

    def print_preorder(self, node):
        if node:
            print(f"{node.data} ")
            self.print_post_order(node.left)
            self.print_post_order(node.right)


    def get_height(self, root, depth):
        if root is None:
            return depth
        else:
            depth += 1
            return max(self.get_height(root.left, depth), self.get_height(root.right, depth))


__name__ = "__main__"

bt = BinaryTree()
bt.add(50)
bt.add(41)
bt.add(10)
bt.add(30)
bt.add(25)
bt.add(6)
bt.add(7)
bt.add(69)

bt.print_in_order(bt.root)
print()
bt.print_post_order(bt.root)
print()
bt.print_preorder(bt.root)
print()
print(bt.get_height(bt.root, 0))