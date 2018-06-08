# -*- coding: utf-8 -*-
__author__ = 'CLH'


class Solution(object):
    def findPaths(self, m, n, N, i, j):
        """
        :type m: int
        :type n: int
        :type N: int
        :type i: int
        :type j: int
        :rtype: int
        """
        if m == 0 or n == 0 or N == 0:
            return 0
        ans_i = i
        ans_j = j
        dp = [[[0 for _ in range(n)] for _ in range(m)] for _ in range(N+1)]
        for k in range(1,N+1):
            for i in range(m):
                for j in range(n):
                    # 考虑i,j 周围四个位置
                    r1 = 1 if i == 0 else dp[k-1][i-1][j]
                    r2 = 1 if i == m-1 else dp[k-1][i+1][j]
                    r3 = 1 if j == 0 else dp[k-1][i][j-1]
                    r4 = 1 if j == n-1 else dp[k-1][i][j+1]
                    dp[k][i][j] = (r1 + r2 + r3 + r4) % 1000000007

        return dp[N][ans_i][ans_j]


if __name__ == "__main__":
    S = Solution()
    print(S.findPaths(m = 1, n = 3, N = 3, i = 0, j = 1))