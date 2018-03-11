__author__ = 'CLH'

import math

class Solution(object):
    def __init__(self):
        self.ans = []
        self.total_ans = []

    def is_palindrome(self,s):
        l = len(s)
        for i in range(math.ceil(l/2)):
            if s[i] != s[l-i-1]:
                return False
        return True

    def backtrack(self,s):
        if s == "":
            self.total_ans.append(list(self.ans))
        else:
            for i in range(1,len(s)+1):
                if self.is_palindrome(s[0:i]):
                    self.ans.append(s[0:i])
                    self.backtrack(s[i:])
                    self.ans.pop()


    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        self.backtrack(s)
        return self.total_ans


if __name__ == "__main__":
    S = Solution()
    print(S.partition("aaab"))
