__author__ = 'CLH'

'''
    Given a string containing only digits, restore it by returning all possible valid IP address combinations.
'''


class Solution:
    def __init__(self):
        self.total_ans = []
        self.ans = []

    def is_legal(self, s):
        # when length bigger than 1, can not begin with 0
        if (len(s)>1 and s[0]=='0'):
            return False
        # must in [0-255]
        elif -1 < int(s) < 256:
            return True
        return False

    def backtrack(self,s,k):
        if s == "" and k == 5:
            self.total_ans.append('.'.join(self.ans))
        # pruning
        elif k == 5 or len(s) < (5-k) or len(s)/3 > (5-k):
            return
        else:
            # enumeration
            for i in range(1,min(4,len(s)+1)):
                if self.is_legal(s[0:i]):
                    self.ans.append(s[0:i])
                    self.backtrack(s[i:], k+1)
                    self.ans.pop()

    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        self.backtrack(s,1)
        return self.total_ans

if __name__ == "__main__":
    S = Solution()
    print(S.restoreIpAddresses("010010"))