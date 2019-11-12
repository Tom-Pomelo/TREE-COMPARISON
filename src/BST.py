from TreeNode import *


class BST(object):
    def __init__(self):
        self.root = None

    def insert(self, val):
        n = Node(val)
        if not self.root:
            self.root = n
        else:
            curr = self.root
            while True:
                if val < curr.val:
                    if curr.left:
                        curr = curr.left
                    else:
                        curr.left = n
                        n.parent = curr
                        break
                elif val > curr.val:
                    if curr.right:
                        curr = curr.right
                    else:
                        curr.right = n
                        n.parent = curr
                        break
                else:
                    curr.val = n.val

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

    def traverse(self):
        self.inorder(self.root)

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.val)
            self.inorder(node.right)
