# -- coding:utf-8 --
__author__ = 'CLH'


class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        r = num
        while r * r > num:
            r = (r + num/r) / 2
        if abs(r*r-num) < 10e-10:
            return True
        else:
            return False


if __name__ == "__main__":
    S = Solution()
    print(S.isPerfectSquare(14))