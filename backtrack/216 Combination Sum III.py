# ! /usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'CLH'

class Solution():
    def __init__(self):
        self.answer = []
        self.total_answer = []
        self.k = 0

    def backtrack(self,k,n):
        if sum(self.answer) == n and k==0:
            self.total_answer.append(list(self.answer))
        elif k==0:
            return
        else:
            if len(self.answer) == 0:
                for i in range(1,10):
                    if i not in self.answer:
                        self.answer.append(i)
                        self.backtrack(k-1,n)
                        self.answer.pop()
                        if k == 0:
                            return
            else:
                for i in range(self.answer[-1],10):
                    if i not in self.answer:
                        self.answer.append(i)
                        self.backtrack(k-1,n)
                        self.answer.pop()
                        if k == 0:
                            return
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        self.k = k
        self.backtrack(k,n)
        return self.total_answer

if __name__ == "__main__":
    S = Solution()
    ans = S.combinationSum3(3,9)
    print(ans)
