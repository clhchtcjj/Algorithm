__author__ = 'CLH'
'''
  给定一个字符串，生成组成这个字符串的字母的全排列(含重复字符)
'''
class solution(object):
    def __init__(self,char_list):
        self.char_list = char_list
        self.answer_list = []
        self.count = 0

    def is_a_solution(self,k):
        return len(self.answer_list) == len(self.char_list)

    def process_solution(self):
        self.count += 1
        print(self.count,self.answer_list)

    def construct_candidates(self,char_list):
        candidates = {} # 字典类型 （字符：出现次数）
        for entry in char_list:
            if candidates.get(entry) is None:
                candidates[entry] = 0
            candidates[entry] += 1
        for entry in self.answer_list:
            candidates[entry] -= 1
        return candidates

    def backtrack(self,k):
        if self.is_a_solution(k):
            self.process_solution()
        else:
            k = k + 1
            candidates = self.construct_candidates(self.char_list)
            for entry in candidates.keys():
                if candidates[entry] != 0:
                    self.answer_list.append(entry)
                    self.backtrack(k)
                    self.answer_list.pop()
                    if len(self.answer_list) == len(self.char_list):
                        return

if __name__=="__main__":
    s = solution(list("aabbcc"))
    s.backtrack(0)


