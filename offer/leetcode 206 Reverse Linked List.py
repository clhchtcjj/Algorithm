__author__ = 'CLH'

# 反转链表中的节点
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    # def reverseList(self, head):
    #     """
    #     :type head: ListNode
    #     :rtype: ListNode
    #     """
    #     if head is None:
    #         return None
    #     elif head.next is None:
    #         return head
    #     else:
    #         pre = None
    #         while head is not None:
    #             curr = head
    #             head = head.next
    #             curr.next = pre
    #             pre = curr
    #         return  pre

    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return self._reverseList(head)

    def _reverseList(self,node,pre=None):
        if not node:
            return pre
        else:
            n = node.next
            node.next = pre
            return self._reverseList(n,node)


if __name__ == "__main__":
    head = ListNode('1')
    head.next = ListNode("2")
    head.next.next = ListNode("3")
    S = Solution()
    S.reverseList(head)
    print(head)


