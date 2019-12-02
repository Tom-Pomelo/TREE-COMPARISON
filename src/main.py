from BST import *
from AVL import *
from BTree import *
from testcase import *
import os
import pickle


def main():
    nums = [10, 50, 100, 500, 1000, 5000]
    generate_tree(nums)
    for opt in range(3):
        if opt == 0:
            T = BST()
        elif opt == 1:
            T = AVL()
        elif opt == 2:
            T = BTree()
        file_name = '../test/' + T.__class__.__name__ + '.pkl'
        if os.path.exists(file_name):
            continue
        res = []
        for n in nums:
            tree = extract_tree_element(n)
            for v in tree:
                T.insert(v)
            cnt = 0
            for v in tree:
                cnt += T.search(v)
            avg = cnt / n
            res.append(avg)
        with open(file_name, 'wb') as f:
            pickle.dump(res, f)
            f.close()
    for opt in range(3):
        if opt == 0:
            T = BST()
        elif opt == 1:
            T = AVL()
        elif opt == 2:
            T = BTree()
        file_name = '../test/' + T.__class__.__name__ + '.pkl'
        with open(file_name, 'rb') as f:
            res = pickle.load(f)
            f.close()
        print(res)


if __name__ == '__main__':
    main()
