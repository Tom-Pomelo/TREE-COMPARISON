import random
import pickle
import os

MAXN = 100


def generate_tree(nums):
    for n in nums:
        generate_tree_element(n)


def generate_tree_element(n):
    file_name = '../test/tree_' + str(n) + '.pkl'
    if os.path.exists(file_name):
        return
    tree = []
    for i in range(n):
        val = random.randint(1, n)
        tree.append(val)
    with open(file_name, 'wb') as f:
        pickle.dump(tree, f)
        f.close()


def extract_tree_element(n):
    file_name = '../test/tree_' + str(n) + '.pkl'
    with open(file_name, 'rb') as f:
        tree = pickle.load(f)
        f.close()
    return tree
