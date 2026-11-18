# bst.py
# An implementation of a binary search tree
# Modified by:

class BSTNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class BST:
    def __init__(self):
        self.root = None
        self.count = 0

    # insert a value into the BST
    # put values that are less than the current node to the left
    # put values that are greater than or equal to the current node
    # to the right
    def insert(self, value):
        if self.root is None:
            self.root = BSTNode(value)
            self.count += 1
            return

        current = self.root

        while True:
            if value < current.value:
                if current.left is None:
                    current.left = BSTNode(value)
                    self.count += 1
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = BSTNode(value)
                    self.count += 1
                    return
                current = current.right

    # return the number of nodes in the BST
    def __len__(self):
        return self.count

    # implement a contains like method that returns if a value is in the BST
    def __contains__(self, value):
        current = self.root

        while current is not None:
            if value == current.value:
                return True
            elif value < current.value:
                current = current.left
            else:
                current = current.right

        return False

    # Helper for inOrderWalk() to call for entire bst
    def in_order_walk(self):
        result = []
        self.in_order_walk_helper(self.root, result)
        return result

    # Walk through the entire tree in ascending order, starting
    # from current, and accumulate the values in the list accumulated
    def in_order_walk_helper(self, current, accumulated):
        if current is None:
            return

        self.in_order_walk_helper(current.left, accumulated)
        accumulated.append(current.value)
        self.in_order_walk_helper(current.right, accumulated)

    # Return the minimum value in the BST or None if the BST is empty
    def minimum(self):
        if self.root is None:
            return None

        current = self.root

        while current.left is not None:
            current = current.left

        return current.value

    # Return the maximum value in the BST or None if the BST is empty
    def maximum(self):
        if self.root is None:
            return None

        current = self.root

        while current.right is not None:
            current = current.right

        return current.value
