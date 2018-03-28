# -*- coding:utf-8 -*-
__author__ = 'CLH'

import Queue

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        last = root
        queue = Queue.Queue()
        queue.put(root)
        nlast = root
        ans = []
        temp = []
        while not queue.empty():
            node = queue.get()
            temp.append(node.val)
            if node.left:
                queue.put(node.left)
                nlast = node.left
            if node.right:
                queue.put(node.right)
                nlast = node.right
            if node == last:
                ans.append(list(temp))
                temp = []
                last = nlast
        return ans

    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ans = self.levelOrder(root)
        ans.reverse()
        return ans
