__author__ = 'CLH'

import Queue
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ans = []
        if root is None:
            return ans
        q = Queue.Queue()
        q.put(root)
        cnt = 1
        while not q.empty():
            size = q.qsize()
            node_list = []
            for i in range(size):
                node = q.get()
                node_list.append(node.val)
                if node.left:
                    q.put(node.left)
                if node.right:
                    q.put(node.right)
            if cnt % 2 == 0:
                node_list.reverse()
                ans.append(node_list)
            else:
                ans.append(node_list)
            cnt += 1
        return ans
