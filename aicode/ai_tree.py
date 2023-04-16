class Node:
    def __init__(self, value, left_child=None, right_child=None):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child

    def search(self, value):
        if self.value == value:
            return self
        elif value < self.value and self.left_child:
            return self.left_child.search(value)
        elif value > self.value and self.right_child:
            return self.right_child.search(value)
        else:
            return None

    def insert(self, value):
        if value < self.value:
            if self.left_child is None:
                self.left_child = Node(value)
            else:
                self.left_child.insert(value)
        elif value > self.value:
            if self.right_child is None:
                self.right_child = Node(value)
            else:
                self.right_child.insert(value)
        else:
            return

    def delete(self, value):
        if value < self.value and self.left_child:
            if self.left_child.value == value:
                if self.left_child.left_child is None and self.left_child.right_child is None:
                    self.left_child = None
                elif self.left_child.left_child is None:
                    self.left_child = self.left_child.right_child
                elif self.left_child.right_child is None:
                    self.left_child = self.left_child.left_child
                else:
                    smallest_node = self.left_child.right_child.get_smallest()
                    self.left_child.value = smallest_node.value
                    self.left_child.right_child.delete(smallest_node.value)
            else:
                self.left_child.delete(value)
        elif value > self.value and self.right_child:
            if self.right_child.value == value:
                if self.right_child.left_child is None and self.right_child.right_child is None:
                    self.right_child = None
                elif self.right_child.left_child is None:
                    self.right_child = self.right_child.right_child
                elif self.right_child.right_child is None:
                    self.right_child = self.right_child.left_child
                else:
                    smallest_node = self.right_child.right_child.get_smallest()
                    self.right_child.value = smallest_node.value
                    self.right_child.right_child.delete(smallest_node.value)
            else:
                self.right_child.delete(value)

    def get_smallest(self):
        if self.left_child is None:
            return self
        else:
            return self.left_child.get_smallest()

class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def search(self, value):
        if self.root is None:
            return None
        else:
            return self.root.search(value)

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self.root.insert(value)

    def delete(self, value):
        if self.root is None:
            return
        else:
            self.root.delete(value)
    
    def get_depth(self, node=None):
        if node is None:
            node = self.root
        if node is None:
            return 0
        else:
            return 1 + max(self.get_depth(node.left_child), self.get_depth(node.right_child))

    def get_height(self, node=None):
        if node is None:
            node = self.root
        if node is None:
            return 0
        else:
            return 1 + max(self.get_height(node.left_child), self.get_height(node.right_child))
