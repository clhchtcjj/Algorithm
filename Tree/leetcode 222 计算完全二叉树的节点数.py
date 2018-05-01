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
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        left = self.countNodes(root.left)
        right = self.countNodes(root.right)
        return left+right+1


    def countNodes2(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        q = Queue.Queue()
        level = 0
        next_level_node = 0
        flag = False
        q.put(root)
        while not q.empty():
            lens = q.qsize()
            level += 1
            for i in range(lens):
                node = q.get()
                next_level_node = 0
                if node.left and node.right:
                    next_level_node += 2
                    q.put(node.left)
                    q.put(node.right)
                elif node.left:
                    next_level_node += 1
                    flag = True
                    break
            if flag:
                break
        return 2**level-1 + next_level_node

    def countNodes3(self,root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        left = self.get_left(root) + 1
        right = self.get_right(root) + 1
        if left == right:
            return (2 << (left-1)) -1
        else:
            return self.countNodes3(root.left) + self.countNodes3(root.right) + 1

    def get_left(self,root):
        count = 0
        while root.left:
            root = root.left
            count += 1
        return count
    def get_right(self,root):
        count = 0
        while root.right:
            root = root.right
            count += 1
        return count

