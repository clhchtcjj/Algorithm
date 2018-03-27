# -*- coding:utf-8 -*-
__author__ = 'CLH'

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        pre,curr = None,pHead
        while curr:
            curr_next = curr.next
            curr.next = pre
            pre = curr
            curr = curr_next
        pHead = pre
        return pHead


    def PrintList(self,pHead):
        node = pHead
        while node:
            print "{} ".format(node.val),
            node = node.next
        print

if __name__ == "__main__":
    head = ListNode(1)
    node = head
    for i in [2,3,4,5,6,7,8]:
        node.next = ListNode(i)
        node = node.next
    S = Solution()
    S.PrintList(head)
    head = S.ReverseList(head)
    S.PrintList(head)
