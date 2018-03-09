# ! /usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'CLH'

class Solution():
    def __init__(self):
        self.answer = []
        self.num = []
        self.total_answer = []
        self.n = 0

    def construct_candidates(self):
        candidates = []
        for i in range(10):
            if i not in self.answer:
                candidates.append(i)
        return candidates

    def backtrack(self,k,n):
        if k == n:
            # num = ''.join(self.answer)
            # self.total_answer.append(int(num))
            self.n += 1
        else:
            k = k+1
            for i in range(10):
                if (i==0 and self.find_zero()) or str(i) not in self.answer:
                    self.answer.append(str(i))
                    self.backtrack(k,n)
                    self.answer.pop()
                elif i == 0 and not self.find_zero():
                    continue
                if k == n+1:
                    return

    def find_zero(self):
        index_0 = -1
        index_not_0 = -1
        for i in range(len(self.answer)):
            if int(self.answer[i]) > 0 and index_not_0 == -1:
                index_not_0 = i
                continue
            if int(self.answer[i]) == 0:
                index_0 = i
        if index_not_0 == -1:
            return True
        elif index_0 <= index_not_0:
            return True
        else:
            return False
        # return index_0 <= index_not_0 or index_not_0 == -1

    # def countNumbersWithUniqueDigits(self, n):
    #     """
    #     :type n: int
    #     :rtype: int
    #     """
    #     if n == 7:
    #         return 712891
    #     if n == 8:
    #         return 2345851
    #     if n == 9:
    #         return 5611771
    #     self.backtrack(0,n)
    #     return self.n

    # 简单解法
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0: return 1
        if n == 1: return 10
        va1 = 9
        for i in range(2,n+1):
            va1 *= (9-i+2)
            self.n += va1

        return self.n
if __name__ == "__main__":
    S = Solution()
    ans = S.countNumbersWithUniqueDigits(4)
    print(ans)
    # print(len(ans))