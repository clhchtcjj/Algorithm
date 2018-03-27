# -*- coding:utf-8 -*-
__author__ = 'CLH'

# 找到链表中的倒数第k个节点

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        start = head
        end = head
        while k and end:
            end = end.next
            k -= 1
        if k > 0:
            return None
        while end:
            start,end = start.next,end.next
        return start

if __name__ == "__main__":
    head = ListNode(1)
    node = head
    for i in [2,3,4,5,6,7,8]:
        node.next = ListNode(i)
        node = node.next
    S = Solution()
    # head = None
    node = S.FindKthToTail(head,1)
    if node:
        print(node.val)

