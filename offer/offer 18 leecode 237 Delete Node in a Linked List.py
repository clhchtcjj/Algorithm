# -- coding:utf-8 --
__author__ = 'CLH'

# 删除链表中指定节点
# 把指定节点的下一节点的内容，复制到要删除的节点，再删除下一节点
# 注意删除尾节点和只有头节点的链表

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next