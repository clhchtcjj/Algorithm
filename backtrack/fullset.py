# -- coding: utf-8 --

'''
求一个集合的全集（回溯法）
'''
# ansset = []
# def is_a_solution(k,n):
# 	return k==n
#
# def construct_candidates():
# 	candidates=[0,1]
# 	num_candidates = 2
# 	return (candidates,num_candidates)
#
# def process_solution(dataset,k,n):
# 	print("{",end="")
# 	for i in range(k):
# 		if ansset[i] != 0:
# 			if i == k-1:
# 				print(dataset[i],end="")
# 			else:
# 				print(dataset[i],end=",")
# 	print("}",end="")
#
# def backtrack(dataset,k,n):
# 	global ansset
# 	if is_a_solution(k,n):
# 		process_solution(dataset,k,n)
# 	else:
# 		k=k+1
# 		current_candidates,num_candidates = construct_candidates()
# 		for i in range(num_candidates):
# 			ansset.append(current_candidates[i])
# 			backtrack(dataset,k,n)
# 			ansset=ansset[0:len(ansset)-1]
# 			if len(ansset) == n:
# 				return

'''
求不重复数字全排列
'''
answer = []
def is_a_solution(k,n):
    return k==n

def process_solution():
    global answer
    for entry in answer:
        print(entry,end=" ")
    print()

def construct_candidates(dataset):
    candidates = []
    for entry in dataset:
        if entry in answer:
            continue
        candidates.append(entry)
    return candidates

def backtrack(dataset,k):
    global answer
    n = len(dataset)
    if is_a_solution(k,n):
        process_solution()
    else:
        k = k + 1
        candidates = construct_candidates(dataset)
        for entry in candidates:
            answer.append(entry)
            backtrack(dataset,k)
            answer.pop()
            if len(answer) == n:
                return

def permutaion(dataset,k):
    global answer
    n = len(dataset)
    if len(dataset) == k:
        print(dataset)
        return
    else:
        for i in range(k,n):
            temp = dataset[k]
            dataset[k] = dataset[i]
            dataset[i] = temp
            permutaion(dataset,k+1)
            temp = dataset[k]
            dataset[k] = dataset[i]
            dataset[i] = temp

if __name__=="__main__":
    ansset = []
    dataset = [5,6,7,8]
    # n = len(dataset)
    backtrack(dataset,0)
    # permutaion(dataset,0)
