# -*- coding: utf-8 -*-
__author__ = 'CLH'

# 判断随机抽取的5张牌是不是顺子
# 思路：用数组模拟牌，先排序，后判断

class Solution:
    def IsContinuous(self, numbers):
        if len(numbers) == 0:
            return False
        # write code here
        numbers = sorted(numbers)
        num_0 = 0
        for i,num in enumerate(numbers[:-1]):
            if num == 0:
                num_0 += 1
            else:
                miss = numbers[i+1]-num - 1
                if miss == -1:
                    return False
                num_0 -= miss
                if num_0 < 0:
                    return False
        return True

if __name__ == "__main__":
    S = Solution()
    print(S.IsContinuous([1,0,3,0,5]))