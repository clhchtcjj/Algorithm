# -*- coding: utf-8 -*-
__author__ = 'CLH'


# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.root = root


    def hasNext(self):
        """
        :rtype: bool
        """
        if not self.root:
            return False
        return True


    def next(self):
        """
        :rtype: int
        """
        if not self.root:
            return
        s = [self.root]
        n = None
        while len(s) != 0:
            node = s[-1]
            if node.left:
                s.append(node.left)
            else:
                n = s.pop()
                break
        num = n.val
        if len(s) == 0:
            self.root = n.right
        else:
            if n.right:
                s[-1].left = n.right
            else:
                s[-1].left = None
        return num







# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
