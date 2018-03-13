__author__ = 'CLH'

'''
    给定n，k，返回元素个数为k的，由1-n不重复数字组成的组合
'''

# class Solution(object):
#     def __init__(self):
#         self.ans = []
#         self.total_ans = []
#
#     def backtrack(self, k, index,n):
#         if len(self.ans) == k:
#             self.total_ans.append(list(self.ans))
#         else:
#             for i in range(index+1,n+1):
#                 self.ans.append(i)
#                 self.backtrack(k,i,n)
#                 self.ans.pop()
#
#     def combine(self, n, k):
#         """
#         :type n: int
#         :type k: int
#         :rtype: List[List[int]]
#         """
#         self.backtrack(k,0,n)
#         return self.total_ans

# 调包解法
from itertools import combinations

class Solution:
    def combine(self, n, k):
        return list(combinations(range(1, n+1), k))

if __name__ == "__main__":
    S = Solution()
    print(S.combine(4,2))
