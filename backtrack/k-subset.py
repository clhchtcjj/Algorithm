__author__ = 'CLH'

'''
  求一个n元集合的k元子集（n>=k>0）
'''


class solution(object):
    def __init__(self,dataset,k):
        self.dataset = dataset
        self.answer = []
        self.k = k

    def is_a_solution(self):
        return len(self.answer) == len(self.dataset)

    def process_solution(self,num):
        count = 0
        for entry in self.answer:
            if entry != 0:
                count += 1
        if count == num:
            for i in range(len(self.answer)):
                if self.answer[i] != 0:
                    print(self.dataset[i],end=" ")
            print()

    def construct_candidates(self):
        candidates = [0,1]
        return candidates

    def backtrack(self,k,num):
        if self.is_a_solution():
            self.process_solution(num)
        else:
            candidates = self.construct_candidates()
            for i in candidates:
                self.answer.append(i)
                self.backtrack(k+1,num)
                self.answer.pop()
                if k == len(self.dataset):
                    return



if __name__ == "__main__":
    num_k = 3
    s = solution([7,2,3,4,5],num_k)
    s.backtrack(0,num_k)



