__author__ = 'CLH'

'''
    Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.  Return a list of all possible strings we could create.
'''
class Solution(object):
    def __init__(self):
        self.S = []
        self.answer = []
        self.total_answer = []

    def is_a_solution(self,k):
        return k == len(self.S)

    def process_solution(self):
        self.total_answer.append(''.join(self.answer))

    def constact_candiates(self, k):
        if self.S[k].isalpha():
            if ord(self.S[k]) > 96:
                return [self.S[k],chr(ord(self.S[k])-32)]
            else:
                return [chr(ord(self.S[k])+32),self.S[k]]
        else:
            return [self.S[k]]

    def backtrack(self,k):
        if self.is_a_solution(k):
            self.process_solution()
        else:
            k = k + 1
            candidates = self.constact_candiates(k-1)
            for ch in candidates:
                self.answer.append(ch)
                self.backtrack(k)
                self.answer.pop()
                if k == len(self.answer):
                    return

    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        self.S = S
        self.backtrack(0)
        return self.total_answer

    # 简单解法
    # def letterCasePermutation(self, S):
    #     ans = [[]]
    #
    #     for char in S:
    #         n = len(ans)
    #         if char.isalpha():
    #             for i in range(n):
    #                 ans.append(ans[i][:])
    #                 ans[i].append(char.lower())
    #                 ans[n+i].append(char.upper())
    #         else:
    #             for i in range(n):
    #                 ans[i].append(char)
    #     # temp = list(map("".join, ans))
    #     # print(temp)
    #     return list(map("".join, ans))

if __name__ == "__main__":
    S = Solution()
    print(S.letterCasePermutation("a1b2"))