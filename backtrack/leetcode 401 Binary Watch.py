# ! /usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'CLH'


# class Solution(object):
#     def __init__(self):
#         self.num = [1,2,4,8,1,2,4,8,16,32] # 4+6每个led灯代表的意思
#         self.answer = [0]*len(self.num) # 可能的解
#         self.total_answer = []
#     def process_solution(self):
#         hour = 0
#         minutes = 0
#         for i in range(len(self.answer)):
#             if i < 4 and self.answer[i]!=0:
#                 hour += self.num[i]*self.answer[i]
#             elif self.answer[i]!=0:
#                 minutes += self.num[i]*self.answer[i]
#         if hour > 11 or minutes > 59:
#             return
#         if minutes < 10:
#             self.total_answer.append("%d:0%d" %(hour,minutes))
#         else:
#             self.total_answer.append("%d:%d" %(hour,minutes))
#
#     def backtrack(self,k,n):
#         if n == 0:
#             self.process_solution()
#         else:
#             k = k + 1
#             if k >= len(self.num)+1:# or n > len(self.num)+1 - k:
#                 return
#             for i in [0,1]:
#                 self.answer[k-1] = i
#                 if i == 0:
#                     self.backtrack(k,n)
#                 else:
#                     self.backtrack(k,n-1)
#                 self.answer[k-1] = 0
#
#                 if n == 0:
#                     return
#
#     def readBinaryWatch(self, num):
#         """
#         :type num: int
#         :rtype: List[str]
#         """
#         self.backtrack(0,num)
#         self.total_answer.reverse()
#         return self.total_answer
#     # 简单解法
#     # def readBinaryWatch(self, num):
#     #     return ['%d:%02d' % (h, m)
#     #             for h in range(12) for m in range(60)
#     #             if (bin(h) + bin(m)).count('1') == num]

class Solution():
    def __init__(self):
        self.num = [1,2,4,8,1,2,4,8,16,32]
        self.answer = [0]*len(self.num)
        self.total_answer = []

    def construct_candidates(self,index):
        candidates = []
        for i in range(index,len(self.answer)):
            if self.answer[i] == 0:
                candidates.append(i)
        return candidates

    def process_solution(self):
        hour = 0
        minutes = 0
        for i in range(len(self.answer)):
            if i < 4 and self.answer[i]!=0:
                hour += self.num[i]*self.answer[i]
            elif self.answer[i]!=0:
                minutes += self.num[i]*self.answer[i]
        if hour > 11 or minutes > 59:
            return
        if minutes < 10:
            self.total_answer.append("%d:0%d" %(hour,minutes))
        else:
            self.total_answer.append("%d:%d" %(hour,minutes))

    def backtrack(self,n,index):
        if n == 0:
            self.process_solution()
        else:
            candidates = self.construct_candidates(index)
            for index in candidates:
                self.answer[index] = 1
                self.backtrack(n-1,index)
                self.answer[index] = 0
                # if n == 0:
                #     return

    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        self.backtrack(num,0)
        # self.total_answer.reverse()
        return self.total_answer

if __name__ == "__main__":
    S = Solution()
    ans = S.readBinaryWatch(2)
    print(ans)
    print(len(ans))
