# -*- coding:utf-8 -*-
__author__ = 'CLH'
# 思路同步走

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        # 计算长度
        len_1 = 0
        len_2 = 0
        if not pHead1 or not pHead2:
            return None
        node = pHead1
        while node:
            len_1 += 1
            node = node.next
        node = pHead2
        while node:
            len_2 += 1
            node = node.next
        minus = abs(len_1-len_2)
        node1 = pHead1
        node2 = pHead2
        if len_1 > len_2:
            cnt = 0
            while cnt < minus:
                node1 = node1.next
                cnt += 1
        else:
            cnt = 0
            while cnt < minus:
                node2 = node2.next
                cnt += 1
        while node1:
            if node1.val == node2.val:
                return node1
            else:
                node1 = node1.next
                node2 = node2.next
        if node1 is None:
            return None

if __name__ == "__main__":
    pHead1 = ListNode(1)
    pHead1.next = ListNode(2)
    phead3 = ListNode(3)
    pHead1.next.next = phead3
    pHead2 = ListNode(4)
    pHead2.next = phead3
    S = Solution()
    S.FindFirstCommonNode(pHead1,pHead2)