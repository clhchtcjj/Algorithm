# -*- coding:utf-8 -*-
__author__ = 'CLH'

#
# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
import Queue
class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return
        q = Queue.Queue()
        q.put(root)
        while not q.empty():
            lens = q.qsize()
            lastnode = None
            for i in range(lens):
                node = q.get()
                if not lastnode:
                    if node.left and node.right:
                        node.left.next = node.right
                        lastnode = node.right
                    elif node.left:
                        lastnode = node.left
                    elif node.right:
                        lastnode = node.right
                else:
                    if node.left and node.right:
                        lastnode.next = node.left
                        node.left.next = node.right
                        lastnode = node.right
                    elif node.left:
                        lastnode.next = node.left
                        lastnode = node.left
                    elif node.right:
                        lastnode.next = node.right
                        lastnode = node.right
                if node.left: q.put(node.left)
                if node.right: q.put(node.right)
            if lastnode:
                lastnode.next = None





