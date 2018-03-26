# -- coding: utf-8 --
__author__ = 'CLH'

# 实现Pow(x, n)

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        # 可以递归的计算
        # 考虑指数为负数的情况
        # 当指数为负的情况，考虑0
        ans = 1.0
        exponent = abs(n)
        if n < 0 and x == 0:
            raise ZeroDivisionError("float division by zero")
        else:
            ans *= self.calculatePow(x,exponent)
        if n < 0:
            return 1.0 / ans
        else:
            return ans

    def calculatePow(self,x,n):
        if n == 0:
            return 1
        elif n == 1:
            return x
        else:
            result = self.calculatePow(x, n>>1)
            result *= result
            if n & 1 == 1:
                result *= x
            return result


if __name__ == "__main__":
    S = Solution()
    print(S.myPow(2.1,3))