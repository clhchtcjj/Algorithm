# -- coding:utf-8 --
__author__ = 'CLH'


# 求一个数n的平方根

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        r = x
        while r*r > x:
            r = (r + x/r) / 2
        return r

if __name__ == "__main__":
    S = Solution()
    print(S.mySqrt(8))