# -*- coding:utf-8 -*-
__author__ = 'CLH'
# 二叉搜索树转化为双向链表
# 思路：中序遍历
#       left指向前驱，right指向后继
#       p_min_node指向当前已生成的链表中尾节点


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def Convert(self, pRootOfTree):
        # write code here
        p_min_node = None
        p_min_node = self.ConvertNode(pRootOfTree,p_min_node)
        pHead = p_min_node
        while pHead and pHead.left:
            pHead = pHead.left
        return pHead

    def ConvertNode(self,root,p_min_node):
        if not root:
            return p_min_node
        pNode = root

        if pNode.left:
            p_min_node = self.ConvertNode(pNode.left,p_min_node)
        pNode.left = p_min_node # 更新当前节点为最后节点
        if p_min_node:
            p_min_node.right = pNode
        p_min_node = pNode # 更新当前节点为最后节点
        if pNode.right:
            p_min_node = self.ConvertNode(pNode.right,p_min_node)
        return p_min_node

if __name__ == "__main__":
    root = TreeNode(1)
    # root.left = TreeNode(5)
    root.right = TreeNode(12)
    # root.left.left = TreeNode(4)
    # root.left.right = TreeNode(7)
    # root.right.left = TreeNode(8)
    root.right.right = TreeNode(13)
    S = Solution()
    S.Convert(root)