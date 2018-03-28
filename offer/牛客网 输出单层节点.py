# -*- coding:utf-8 -*-
__author__ = 'CLH'

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import Queue
class TreeLevel:
    def getTreeLevel(self, root, dep):
        # write code here
        if not root:
            return None
        row = 0
        last = root
        queue = Queue.Queue()
        queue.put(root)
        nlast = root
        head = ListNode(0)
        flag = False
        Lnode = head
        while not queue.empty():
            node = queue.get()
            if node.left:
                queue.put(node.left)
                nlast = node.left
            if node.right:
                queue.put(node.right)
                nlast = node.right
            if dep -1 == row:
                if not flag:
                    Lnode.val = node.val
                    flag = True
                else:
                    Lnode.next = ListNode(node.val)
                    Lnode = Lnode.next
            if dep-1 < row:
                return head
            if last == node:
                last = nlast
                row += 1
                flag = False
        return head

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(5)
    root.right = TreeNode(12)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(7)
    root.right.left = TreeNode(8)
    root.right.right = TreeNode(9)
    S = TreeLevel()
    root = None
    head = S.getTreeLevel(root,3)
    node = head
    while node:
        print "{} ".format(node.val),
        node = node.next

