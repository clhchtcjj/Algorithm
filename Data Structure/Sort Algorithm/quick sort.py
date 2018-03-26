# -- coding: utf-8 --
__author__ = 'CLH'


# 快排
def partition(nums, low, high):
    pivot = nums[low]
    while low < high:
        while low < high and pivot<=nums[high]:
            high -= 1
        nums[low] = nums[high]
        while low < high and pivot>=nums[low]:
            low += 1
        nums[high] = nums[low]
    nums[low] = pivot
    return low


def quick_sort(nums,low,high):
    if low < high:
        index = partition(nums,low,high)
        print index
        quick_sort(nums,low,index-1)
        quick_sort(nums,index+1,high)

# 直接插入排序

def insert_sort(nums):
    for i in range(1,len(nums)-1):
        tmp = nums[i]
        j = 0
        for j in range(i-1,0,-1):
            if tmp > nums[j]:
                nums[j+1] = nums[j]
                break
            nums[j+1] = nums[j]
        nums[j] = tmp
        print nums

def half_insert_sort(nums):
    for i in range(1,len(nums)-1):
        tmp = nums[i]
        low = 0
        high = i-1
        # 找到第一个比它小的
        while low < high:
            mid = (low+high) / 2
            if nums[mid] > tmp:
                high = mid-1
            else:
                low = mid+1
        for j in range(i-1, high, -1):
            nums[j+1] = nums[j]
        nums[high+1] = tmp
        print nums

def xier_sort(nums):
    le = len(nums)
    dk = le/2
    while dk >= 1:
        for i in range(dk, le):
            if nums[i] < nums[i-dk]:
                tmp = nums[i]
                j = 0
                for j in range(i-dk,-1,-dk):
                    if nums[j] < tmp:
                        j += dk
                        break
                    else:
                        nums[j+dk] = nums[j]
                nums[j] = tmp
        dk /= 2
        print(nums)

def bubble_sort(nums):
    for i in range(0,len(nums)-1):
        flag = False
        for j in range(len(nums)-1,i,-1):
            if nums[j] < nums[j-1]:
                nums[j],nums[j-1] = nums[j-1],nums[j]
                flag = True
        if not flag:
            return


if __name__ == "__main__":
    nums = [5,4,1,3,2,8]
    print(nums)
    # quick_sort(nums,0,5)
    bubble_sort(nums)
    print(nums)