# -*- coding: utf-8
__author__ = 'CLH'

# 思路: 中序遍历，计算两者之间的差
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ans = [None] # 记录当前最小绝对值差
        lastnode = [None] # 记录已经按序遍历的最后一个节点
        self.getMinimunDifferenceCore(root,lastnode,ans)
        return ans[0]

    def getMinimunDifferenceCore(self,node,lastnode,ans):
        if node is None:
            return
        if node.left:
            self.getMinimunDifferenceCore(node.left,lastnode,ans)
        # 处理根
        if lastnode[0] is not None:
            tmp = abs(lastnode[0].val - node.val)
            if ans[0] is None or ans[0] > tmp:
                ans[0] = tmp
        lastnode[0] = node # 更新已经按序遍历的最后一个节点
        if node.right:
            self.getMinimunDifferenceCore(node.right,lastnode,ans)


