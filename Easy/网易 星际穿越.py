__author__ = 'CLH'

import math
class Solution():
    def __init__(self,h):
        self.h = h
        self.x = int(math.sqrt(h))

    def calculate(self):
        for x in range(self.x+1,0,-1):
            if x*(x-1) <= self.h:
                return x-1
        return -1


if __name__ == "__main__":
    h = int(input())
    S = Solution(h)
    print(S.calculate())