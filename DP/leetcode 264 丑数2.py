# -*- coding: utf-8 -*-
__author__ = 'CLH'

import heapq

class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 超时
        # if n == 0:
        #     return 0
        # if n == 1:
        #     return 1
        # dp = [1]
        # ans = [(2,2)]
        # cnt = 1
        # while cnt < n:
        #     # print ans
        #     # print dp
        #     tmp = -1
        #     index = -1
        #     f = -1
        #     for i, (num, F) in enumerate(ans):
        #         if tmp == -1 or tmp > num:
        #             tmp = num
        #             index = i
        #             f = F
        #     if f == 5:
        #         if index == 0:
        #             ans = ans[1:]
        #         else:
        #             ans[index] = float('inf')
        #     elif f == 3:
        #         ans[index] = (tmp / 3 * 5, 5)
        #     else:
        #         ans[index] = (tmp / 2 * 3, 3)
        #     if tmp <= dp[-1]:
        #         continue
        #     dp.append(tmp)
        #     ans.append((tmp*2, 2))
        #     cnt += 1
        # return dp[-1]

        # 利用堆
        heap = []
        heapq.heappush(heap, 1)
        ans = 0
        while n > 0:
            while heap and heap[0] <= ans: # remove duplicate ugly number
                heapq.heappop(heap)
            ans = heapq.heappop(heap)
            n -= 1
            heapq.heappush(heap, ans * 2)
            heapq.heappush(heap, ans * 3)
            heapq.heappush(heap, ans * 5)
        return ans