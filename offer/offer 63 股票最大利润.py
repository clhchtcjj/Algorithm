# -*- coding:utf-8 -*-
__author__ = 'CLH'

# 股票最大利润
# 思路：扫描一遍数组，以当前元素为卖出时刻，只要找到它前面的最小值，就能得到此刻卖出所能获得的最大利润了
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0

        max_profit = prices[1]-prices[0]
        min_price = min(prices[0],prices[1])
        for j in range(2,len(prices)):
            curr_profit = prices[j] - min_price
            if curr_profit > max_profit:
                max_profit = curr_profit
            if min_price > prices[j]:
                min_price = prices[j]
        if max_profit>0:
            return max_profit
        else:
            return 0

    def maxProfit_2(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        sum_profit = 0
        max_profit = 0
        min_price = prices[0]
        for j in range(1,len(prices)):
            curr_profit = prices[j] - min_price
            if prices[j]-prices[j-1] < 0:
                min_price = prices[j]
                sum_profit += max_profit
                max_profit = 0
            else:
                if j == len(prices)-1:
                    sum_profit += curr_profit
                if curr_profit > max_profit:
                    max_profit = curr_profit
                if min_price > prices[j]:
                    min_price = prices[j]


    def maxProfit_3(self, prices):
        '''
        最多进行两次交易的最大利润：其实就是找分为点
        :param prices:
        :return:
        '''
        if len(prices) < 2:
            return 0
        min_price = prices[0]
        first = [0]
        second = [0,0]
        for i in range(1,len(prices)):
            max_profit = prices[i]-min_price
            first.append(max_profit)
            if min_price > prices[i]:
                min_price = prices[i]
        max_price = prices[-1]
        max_profit = - float('inf')
        for i in range(len(prices)-3,-1,-1):
            max_profit = max(max_profit,max_price - prices[i+1])
            second.append(max_profit)
            if max_price < prices[i+1]:
                max_price = prices[i+1]
        second.reverse()
        print(first,second)
        max_profit = -float('inf')
        sum_profit = list(map(lambda x: x[0]+x[1], zip(first, second)))
        for i in range(len(prices)):
            if max_profit < max(first[i],sum_profit[i]):
                max_profit = max(first[i],sum_profit[i])
        return max_profit

    def maxProfit_4(self, prices,k):
        '''
        最多进行k次交易
        dp思想，维护两个变量local[i][j]第i天，进行第j次交易的最大收益 global[i][j]第i天，进行了j次交易的最大收益
        :param prices:
        :return:
        '''
        if len(prices) < 2:
            return 0
        if k < 1:
            return 0
        if k > len(prices) // 2: # 进行任意次
            sum = 0
            for i in range(1,len(prices)):
                if prices[i]-prices[i-1] > 0:
                    sum += prices[i]-prices[i-1]
            return sum
        local = [[0 for i in range(k+1)] for j in range(len(prices))]
        glob = [[0 for i in range(k+1)] for j in range(len(prices))]
        for i in range(1,len(prices)):
            diff = prices[i] - prices[i-1]
            for j in range(1,k+1):
                # 可以当天买卖
                local[i][j] = max(glob[i-1][j-1] + max(0,diff),local[i-1][j]+diff)
                glob[i][j] = max(glob[i-1][j],local[i][j])
        return glob[len(prices)-1][k]



if __name__ == "__main__":

    S = Solution()
    print(S.maxProfit_4([2,1,2,0,1],2))
