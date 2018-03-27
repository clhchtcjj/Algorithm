# -*- coding:utf-8 -*-
__author__ = 'CLH'

# 链表中环的入口
# 定义一个快指针，一个慢指针，慢的追上快的，则一点有环
# 重新定义两个指针，其中一个指针比另一个多走环中节点数目步，当两个指针相遇时，即为入口节点

# 也可以用hashTable实现
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 判断是否有环
        fast_node = head
        slow_node = head
        flag = False
        while slow_node and fast_node and fast_node.next:
            fast_node = fast_node.next.next
            slow_node = slow_node.next
            if fast_node == slow_node:
                flag = True
                break
        # 有环，统计数目
        cnt = 1
        if flag:
            node = fast_node
            while node.next!=fast_node:
                cnt += 1
                node = node.next
            # 找入口
            slow_node = head
            fast_node = head
            while cnt:
                fast_node = fast_node.next
                cnt -= 1
            while slow_node != fast_node:
                slow_node,fast_node = slow_node.next,fast_node.next
            return slow_node
        else:
            return None

if __name__ == "__main__":

    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = head

    S = Solution()
    node = S.detectCycle(head)
    if node:
        print(S.detectCycle(head).val)



