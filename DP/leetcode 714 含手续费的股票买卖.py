# -*- coding: utf-8 -*-
__author__ = 'CLH'


class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        n = len(prices)
        if n == 0:
            return 0
        A = [0 for _ in range(n)]
        B = [0 for _ in range(n)]
        A[0] = A[0] - prices[0]
        for i in range(1, n ):
            A[i] = max(A[i-1], B[i-1]-prices[i])
            B[i] = max(B[i-1], A[i-1]+prices[i]-fee)
        return B[n-1]

if __name__ == "__main__":
    S = Solution()
    print(S.maxProfit(prices = [1, 3, 2, 8, 4, 9], fee = 2))
