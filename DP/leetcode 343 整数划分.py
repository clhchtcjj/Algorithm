# -*- coding: utf-8 -*-
__author__ = 'CLH'


class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        dp = [0,1]
        print n
        for i in range(2,n+1):
            # print i, dp
            tmp_x = i // 2
            tmp_y = i - tmp_x
            candidate = []
            x = tmp_x
            y = tmp_y
            while x >= 1:
                x_,y_ = x,y
                if dp[x] > x:
                    x_ = dp[x]
                if dp[y] > y:
                    y_ = dp[y]
                candidate.append(x_*y_)
                x -= 1
                y += 1
            dp.append(max(candidate))
        return dp[-1]

    # 另解
    """
    2  ->  1 * 1
    3  ->  2 * 1
    4  ->  2 * 2
    5  ->  3 * 2
    6  ->  3 * 3
    7  ->  3 * 2 * 2
    8  ->  3 * 3 * 2
    9  ->  3 * 3 * 3
    10 ->  3 * 3 * 2 * 2
    11 ->  3 * 3 * 3 * 2
    12 ->  3 * 3 * 3 * 3
    13 ->  3 * 3 * 3 * 2 * 2

    n / 3 <= 1 时，分为两个数的乘积，尽量均摊
    n / 3 > 1 时，分为若干个3和2的乘积
    n % 3 == 0 时，分为n个3的乘积
    n % 3 == 1 时，分为n-1个3和两个2的乘积
    n % 3 == 2 时，分为n个3和一个2的乘积
    """
    # div = n / 3
    # if div <= 1:
    #     return (n / 2) * (n / 2 + n % 2)
    # mod = n % 3
    # if mod == 0:
    #     return 3 ** div
    # elif mod == 1:
    #     return 3 ** (div - 1) * 4
    # elif mod == 2:
    #     return 3 ** div * 2