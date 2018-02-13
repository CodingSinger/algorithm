

#deepcopy的效率很慢 能不用尽量不用

#切片 > copy > deepcopy 数组的复制性能





#冒泡排序
# 比较每两个元素，交换位置
# 经过n*n次比较之后，数组就会有序 可以看出该方法简单但是运行效率低下
import random

import time
import copy


def bubbleSort(nums):

    for  i in range(len(nums)-1):
        for j in range(i+1,len(nums)):

            if nums[i]>nums[j]:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp


#选择排序
# 思路：从数组中获得最小的数据，与数组的第一个交换位置，然后依次从接下来的数组第2到最后位置再次选出最小的，与第2个数据交换位置，依次类推。
def selectionSort(nums):

    for i in range(len(nums)):
        min1 = nums[i]
        minIndex = i
        for j in range(i+1,len(nums)):
            if min1 > nums[j]:
                min1 = nums[j]
                minIndex = j


        #放在排好的部分的最后 交换位置


        temp = nums[i]

        nums[i] = nums[minIndex]

        nums[minIndex] = temp

# 直接插入排序
# 直接插入排序是一种简单的插入排序法，其基本思想是：把待排序的记录按其关键码值的大小逐个插入到一个已经排好序的有序序列中，直到所有的记录插入完为止，得到一个新的有序序列。[1]
# 例如,已知待排序的一组记录是：
# 60,71,49,11,24,3,66
# 假设在排序过程中，前3个记录已按关键码值递增的次序重新排列，构成一个有序序列：
# 49,60,71
# 将待排序记录中的第4个记录（即11）插入上述有序序列，以得到一个新的含4个记录的有序序列。首先，应找到11的插入位置，再进行插入。可以讲11放入数组的第一个单元r[0]中，这个单元称为监视哨，
# 然后从71起从右到左查找，11小于71，将71右移一个位置，11小于60，又将60右移一个位置，11小于49，又再将49右移一个位置，这时再将11与r[0]的值比较，11≥r[0]，它的插入位置就是r[1]。假设11大于第一个值r[1]。
# 它的插入位置应该在r[1]和r[2]之间，由于60已经右移了，留出来的位置正好留给11.后面的记录依照同样的方法逐个插入到该有序序列中。若记录数n,续进行n-1趟排序，才能完成。


def insertSort(nums):

    for i in range(1,len(nums)):
        # for j in range(0,i):
        #     if nums[i] <nums[j]:
        #         #插入
        #
        #
        #         #因为python列表的固有方法，如下代替数组的右移过程和插入过程
        #         nums.insert(j,nums[i])
        #         nums.pop(i+1)

        num = nums[i]
        for j in range(i-1,-1,-1):
            if num < nums[j]:
                nums[j+1] = nums[j]
                if j == 0: #如果为0，则说明该num应该插入最前面
                    nums[j] = num
            else:
                nums[j+1] = num
                break


def shellSort(nums):

    lens = len(nums)

    # gap = len //3
    #
    # c = gap /3 if len /3 == len //3 else gap //3+1
    #

    gap = lens //2
    def swap(nums,i,j):

        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp


    while gap >=1:




        # for j in range(gap): #用行列来确定一个点
        #
        #     for k in range(1,c+1):
        #
        #         num = nums[j+k*gap] #引用行列来确定一个点
        #
        #         #比较该num和这个num这个列之前的那些数 进行插入 因此又需要一个for循环  能不用行列确定一个点的尽量不用行列
        #


        for i in range(gap,len(nums)):

            k = i
            for j in range(i-gap,-1,-gap):
                if nums[j] > nums[k]:
                    swap(nums,k,j) #这里为了方便 用直接交换代替后移和插入 后移和插入做法可以根据上面插入排序
                    k = j #因为交换过 所以下标变化





        gap = gap//2







def merge(a, b):
    c = []
    h = j = 0
    while j < len(a) and h < len(b):
        if a[j] < b[h]:
            c.append(a[j])
            j += 1
        else:
            c.append(b[h])
            h += 1

    if j == len(a):
        for i in b[h:]:
            c.append(i)
    else:
        for i in a[j:]:
            c.append(i)

    return c


def merge_sort(lists):
    if len(lists) <= 1:
        return lists
    middle = int(len(lists)/2)
    left = merge_sort(lists[:middle])
    right = merge_sort(lists[middle:])
    return merge(left, right)







# 归并排序

# 思路:通过递归将一个大数组对半再对半...截取成小数组进行合并，在合并的时候就根据大小进行了排序，然后又把小数组合并成大数组，即每一次合并都是排序的

def mergeSort(nums):

    #通常最简单的是将两个数组比较按大小顺序归并到第三个数组
    #这里直接在原数组上进行改动归并 原地归并
    def merge(a,low,mid,high):

        copyw = a[low:high+1]


        #为什么要减去Low，因为这里copyw是切片，a[low..high+1]映射成copyw[0..high+1-low]

        d = mid+1-low #右半边指针
        k = low-low # 左半边指针

        for i in range(low,high+1):

            if d> high-low:
                a[i] = copyw[k]
                k+=1
            elif k > mid-low:
                a[i] = copyw[d]
                d+=1
            elif copyw[d]>copyw[k]:
                a[i] = copyw[k]
                k+=1

            else:
                a[i] = copyw[d]
                d+=1



    def sort(nums,low,high):
        if high <= low:
            return

        #拆分

        mid = (int)(low+(high-low)/2)

        sort(nums,low,mid) #左半边递归排序
        sort(nums,mid+1,high) #右半边递归排序
        merge(nums,low,mid,high) #合并成一个有序的


    sort(nums,0,len(nums)-1)










































if __name__ == '__main__':




    n = 4000

    arr = []
    for i in range(n):
        arr.append(random.randint(0,1000))



    print("原始数组",arr)
    start1 = time.time()

    insertSort(arr.copy())

    print(time.time()-start1)
    start2 = time.time()

    shellSort(arr.copy())

    print(time.time() - start2)

    start3 = time.time()

    selectionSort(arr.copy())


    c = copy.deepcopy(arr)
    print(time.time() - start3)


    start4 = time.time()
    arr4 = arr.copy()
    mergeSort(arr4)

    print(time.time()-start4)

    start5 = time.time()
    arr5 = arr.copy()

    arr5 = merge_sort(arr5)
    print(time.time()-start5)
    print(arr5)
    print(arr4)








