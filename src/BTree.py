import bisect
from queue import *


class BNode(object):
    def __init__(self, tree, contents = None, children = None):
        self.tree = tree
        self.contents = contents or []
        self.children = children or []

    def lateral(self, parent, parent_index, destination, destination_index):
        if parent_index > destination_index:
            destination.contents.append(parent.contents[destination_index])
            parent.contents[destination_index] = self.contents.pop(0)
            if self.children:
                destination.children.append(self.children.pop(0))
        else:
            destination.contents.insert(0, parent.contents[parent_index])
            parent.contents[parent_index] = self.contents.pop()
            if self.children:
                destination.children.insert(0, self.children.pop())

    def shrink(self, ancestors):
        parent = None

        if ancestors:
            parent, parent_index = ancestors.pop()
            # try to lend to the left neighboring sibling
            if parent_index:
                left_sib = parent.children[parent_index - 1]
                if len(left_sib.contents) < self.tree.order:
                    self.lateral(parent, parent_index, left_sib, parent_index - 1)
                    return

            # try the right neighbor
            if parent_index + 1 < len(parent.children):
                right_sib = parent.children[parent_index + 1]
                if len(right_sib.contents) < self.tree.order:
                    self.lateral(parent, parent_index, right_sib, parent_index + 1)
                    return

        sibling, push = self.split()

        if not parent:
            parent, parent_index = self.tree.BRANCH(self.tree, children = [self]), 0
            self.tree.root = parent

        # pass the median up to the parent
        parent.contents.insert(parent_index, push)
        parent.children.insert(parent_index + 1, sibling)
        if len(parent.contents) > parent.tree.order:
            parent.shrink(ancestors)

    def split(self):
        center = len(self.contents) // 2
        median = self.contents[center]
        sibling = type(self)(
            self.tree,
            self.contents[center + 1:],
            self.children[center + 1:])
        self.contents = self.contents[:center]
        self.children = self.children[:center + 1]
        return sibling, median

    def insert(self, index, item, ancestors):
        self.contents.insert(index, item)
        if len(self.contents) > self.tree.order:
            self.shrink(ancestors)


class BTree(object):
    BRANCH = LEAF = BNode

    def __init__(self, order):
        self.order = order
        self.root = self._bottom = BNode(self)

    def get_path_to(self, item):
        current = self.root
        ancestors = []

        while current.children is None:
            index = bisect.bisect_left(current.contents, item)
            ancestors.append((current, index))
            if index < len(current.contents) and current.contents[index] == item:
                return ancestors
            current = current.children[index]

        index = bisect.bisect_left(current.contents, item)
        ancestors.append((current, index))
        return ancestors

    def insert(self, item):
        ancestors = self.get_path_to(item)
        node, index = ancestors[-1]
        while node.children is None:
            node = node.children[index]
            index = bisect.bisect_left(node.contents, item)
            ancestors.append((node, index))
        node, index = ancestors.pop()
        node.insert(index, item, ancestors)

    def level_order(self):
        vec = []
        q = Queue()
        q.put(self.root)
        while not q.empty():
            v = []
            for i in range(q.qsize()):
                n = q.get()
                v.append(n.contents)
                for n in n.children:
                    q.put(n)
            vec.append(v)
        print(vec)
