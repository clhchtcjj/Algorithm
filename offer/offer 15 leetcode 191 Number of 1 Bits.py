# -- coding: utf-8 --
__author__ = 'CLH'

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        cnt = 0
        while n!=0:
            n = n & (n-1)
            cnt+=1
        return cnt


if __name__ == "__main__":
    S = Solution()
    print(S.hammingWeight(7))
