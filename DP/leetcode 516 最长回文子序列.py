# -*- coding: utf-8 -*-
__author__ = 'CLH'



class Solution(object):
    def longestPalindromeSubseq(self, s):
        """Palindromic
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n == 0:
            return 0
        if n == 1:
            return 1
        dp = [[0 for i in range(n)] for i in range(n)]
        for i in range(n-1,-1,-1):
            dp[i][i] = 1
            for j in range(i+1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1]+2
                else:
                    dp[i][j] = max(dp[i+1][j],dp[i][j-1])
        return dp[0][n-1]
if __name__ == "__main__":
    S = Solution()
    print(S.longestPalindromeSubseq("abba"))

