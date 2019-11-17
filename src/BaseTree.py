class Tree(object):
    def __init__(self):
        self.root = None

    def insert(self, val):
        pass

    def search(self, val):
        pass

    def traverse(self):
        self.inorder(self.root)

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.val)
            self.inorder(node.right)
