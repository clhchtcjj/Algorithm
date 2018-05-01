# -*- coding:utf-8 -*-
__author__ = 'CLH'

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import Queue
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        q = Queue.Queue()
        q.put(root)
        ans = []
        while not q.empty():
            lens = q.qsize()
            for i in range(lens):
                node = q.get()
                if node.left:
                    q.put(node.left)
                if node.right:
                    q.put(node.right)
                if i == lens-1:
                    ans.append(node.val)
        return ans