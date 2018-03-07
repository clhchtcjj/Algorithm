# ! /usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'CLH'

'''
526. Beautiful Arrangement
    Suppose you have N integers from 1 to N.
    We define a beautiful arrangement as an array that is constructed by these N numbers successfully
    if one of the following is true for the ith position (1 <= i <= N) in this array:
    (1) The number at the i-th position is divisible by i.
    (2) i is divisible by the number at the i-th position.
    Now given N, how many beautiful arrangements can you construct?
'''

class Solution(object):
    def __init__(self):
        self.N = 0
        self.total_num = 0

    def backtrack(self, k):
        if k == self.N:
            self.total_num += 1
        else:
            k = k + 1
            for i in range(1, self.N+1):
                if i % k == 0 or k % i == 0:
                    if self.visited[i] == 1:
                        continue
                    self.visited[i] = 1
                    self.backtrack(k)
                    self.visited[i] = 0
                    if k == self.N:
                        return

    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        self.N = N
        self.visited = [0]*(N+1)
        self.backtrack(0)
        return self.total_num


if __name__ == "__main__":
    S = Solution()
    S.countArrangement(15)





