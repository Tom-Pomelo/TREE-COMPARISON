from TreeNode import *
from BaseTree import *


class BST(Tree):
    def insert_helper(self, node, val):
        if not node:
            node = Node(val)
            return node
        if val < node.val:
            node.left = self.insert_helper(node.left, val)
        elif val > node.val:
            node.right = self.insert_helper(node.right, val)
        return node

    def insert(self, val):
        self.root = self.insert_helper(self.root, val)

    def search_helper(self, node, val):
        if not node:
            return None
        elif node.val == val:
            return node
        elif node.val < val:
            return self.search_helper(node.left, val)
        else:
            return self.search_helper(node.right, val)

    def search(self, val):
        return self.search_helper(self.root, val)
