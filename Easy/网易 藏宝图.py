__author__ = 'CLH'

class Solution():
    def __init__(self,s,t):
        self.s = s
        self.t = t

    def is_substring(self):
        k = 0
        flag = "No"
        i = 0
        while(i < len(self.t)):
            if k == len(self.s):
                break
            for j in range(k,len(self.s)):
                k = j+1
                if self.s[j] == self.t[i]:
                    if i == len(self.t)-1:
                        flag = "Yes"
                    i = i+1
                    break
        return flag

if __name__ == "__main__":
    s = input().strip()
    t = input().strip()
    S = Solution(s,t)
    print(S.is_substring())



