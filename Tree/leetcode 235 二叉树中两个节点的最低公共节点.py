# -*- coding: utf-8 -*-
__author__ = 'CLH'


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        s_node = []
        s_flag = []
        path1 = [] # 会有重复值
        path2 = []  # 会有重复值
        node = root
        while node or len(s_node) != 0:
            while node:
                s_node.append(node)
                s_flag.append(1)
                if node == p:
                    path1.append(list(s_node))
                if node == q:
                    path2.append(list(s_node))
                node = node.left
            while len(s_flag) != 0 and s_flag[-1] == 2:
                s_flag.pop()
                s_node.pop()
            if len(s_flag) != 0:
                s_flag[-1] = 2
                node = s_node[-1]
                node = node.right
            if node == root:
                break
        if len(path1) == 0 or len(path2) == 0:
            return None
        cnt = -1
        path = None
        for p1 in path1:
            for p2 in path2:
                tmp = 0
                len1 = len(p1)
                len2 = len(p2)
                for i in range(min(len1,len2)):
                    if p2[i] == p1[i]:
                        tmp = i
                    else:
                        break
                if cnt < tmp:
                    path = p2
                    cnt = tmp
        return path[cnt]
