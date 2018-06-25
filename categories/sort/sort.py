# deepcopy的效率很慢 能不用尽量不用

# 切片 > copy > deepcopy 数组的复制性能





# 冒泡排序
# 比较每两个元素，交换位置
# 经过n*n次比较之后，数组就会有序 可以看出该方法简单但是运行效率低下
import random

import time
import copy

import math


def bubbleSort(nums):
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):

            if nums[i] > nums[j]:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp


# 选择排序
# 思路：从数组中获得最小的数据，与数组的第一个交换位置，然后依次从接下来的数组第2到最后位置再次选出最小的，与第2个数据交换位置，依次类推。
def selectionSort(nums):
    for i in range(len(nums)):
        min1 = nums[i]
        minIndex = i
        for j in range(i + 1, len(nums)):
            if min1 > nums[j]:
                min1 = nums[j]
                minIndex = j

        # 放在排好的部分的最后 交换位置


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
    for i in range(1, len(nums)):
        # for j in range(0,i):
        #     if nums[i] <nums[j]:
        #         #插入
        #
        #
        #         #因为python列表的固有方法，如下代替数组的右移过程和插入过程
        #         nums.insert(j,nums[i])
        #         nums.pop(i+1)

        num = nums[i]
        for j in range(i - 1, -1, -1):
            if num < nums[j]:  # 如果num<nums[j]，则让nums[j]往后移，因为num需要继续往前寻找
                nums[j + 1] = nums[j]
                if j == 0:  # 如果为0，则说明该num应该插入最前面
                    nums[j] = num
            else:
                nums[j + 1] = num  # num>num[j]，则num需要排到num
                break


# 希尔排序
def shellSort(nums):
    lens = len(nums)

    # gap = len //3
    #
    # c = gap /3 if len /3 == len //3 else gap //3+1
    #

    gap = lens // 2

    def swap(nums, i, j):

        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp

    while gap >= 1:

        # for j in range(gap): #用行列来确定一个点
        #
        #     for k in range(1,c+1):
        #
        #         num = nums[j+k*gap] #引用行列来确定一个点
        #
        #         #比较该num和这个num这个列之前的那些数 进行插入 因此又需要一个for循环  能不用行列确定一个点的尽量不用行列
        #


        for i in range(gap, len(nums)):

            k = i
            for j in range(i - gap, -1, -gap):
                if nums[j] > nums[k]:
                    swap(nums, k, j)  # 这里为了方便 用直接交换代替后移和插入 后移和插入做法可以根据上面插入排序
                    k = j  # 因为交换过 所以下标变化

        gap = gap // 2


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
    middle = int(len(lists) / 2)
    left = merge_sort(lists[:middle])
    right = merge_sort(lists[middle:])
    return merge(left, right)


# 归并排序

# 思路:通过递归将一个大数组对半再对半...截取成小数组进行合并，在合并的时候就根据大小进行了排序，然后又把小数组合并成大数组，即每一次合并都是排序的

def mergeSort(nums):
    # 通常最简单的是将两个数组比较按大小顺序归并到第三个数组
    # 这里直接在原数组上进行改动归并 原地归并
    def merge(a, low, mid, high):

        copyw = a[low:high + 1]

        # 为什么要减去Low，因为这里copyw是切片，a[low..high+1]映射成copyw[0..high+1-low]

        d = mid + 1 - low  # 右半边指针
        k = low - low  # 左半边指针

        for i in range(low, high + 1):

            if d > high - low:
                a[i] = copyw[k]
                k += 1
            elif k > mid - low:
                a[i] = copyw[d]
                d += 1
            elif copyw[d] > copyw[k]:
                a[i] = copyw[k]
                k += 1

            else:
                a[i] = copyw[d]
                d += 1

    def sort(nums, low, high):
        if high <= low:
            return

        # 拆分

        mid = (int)(low + (high - low) / 2)

        sort(nums, low, mid)  # 左半边递归排序
        sort(nums, mid + 1, high)  # 右半边递归排序
        merge(nums, low, mid, high)  # 合并成一个有序的

    sort(nums, 0, len(nums) - 1)


def quicksort(lst, lo, hi):
    if lo < hi:
        p = partition(lst, lo, hi)
        quicksort(lst, lo, p)
        quicksort(lst, p + 1, hi)
    return


def partition(lst, lo, hi):
    pivot = lst[hi - 1]
    i = lo - 1
    for j in range(lo, hi):
        if lst[j] < pivot:
            i += 1
            lst[i], lst[j] = lst[j], lst[i]
    if lst[hi - 1] < lst[i + 1]:
        lst[i + 1], lst[hi - 1] = lst[hi - 1], lst[i + 1]
    return i + 1


def quicksort2(a, p, q):
    if p < q:
        r = partition2(a, p, q)
        # 对r的左右两部分继续排序
        quicksort2(a, p, r)
        quicksort2(a, r + 1, q)


def partition2(a, p, q):
    guard = a[p]  # 设置哨兵

    temp = p
    for i in range(p + 1, q):
        # 遍历，将小于哨兵的元素移到前面去，temp相当于隔离小于哨兵和大于哨兵元素的一个分界点。
        if a[i] <= guard:
            # 移动
            # 分界点往前腾出一个位置
            temp += 1
            # 此时a[temp]是大于哨兵的一个元素，和小于哨兵的元素交换位置
            a[temp], a[i] = a[i], a[temp]

    # 循环完后，发现temp及temp之前的都是小于guard的，temp之后的都是大于或者等于guard的,将a[p]和a[temp]换个位置，则能明确地划分出来 ,并且这表示这个guard在这个数组的位置已经确定了在temp。

    a[temp], a[p] = a[p], a[temp]

    return temp  #


# 推荐这种算法

def quicksort3(a, p, q):
    if p < q:
        r = partition3(a, p, q)
        # 对r的左右两部分继续排序
        quicksort3(a, p, r)
        quicksort3(a, r + 1, q)


# p为起点，q为数组重终点(可取到)
def partition3(a, p, q):
    guard = a[p]
    temp = p
    #重合时，退出循环
    while p < q:
        #一定要从右边找起，从右边找到比哨兵小的
        while p < q and a[q] >= guard:
            q -= 1
        #从左边找比哨兵大的
        while p < q and a[p] <= guard:
            p += 1
        #交换大小
        if p < q:
            a[p], a[q] = a[q], a[p]

    # 哨兵数归位
    a[temp], a[p] = a[p], a[temp]
    return p


## 堆排序


def heapSortAsc(arr):
    # 构建大顶堆
    # 叶子节点n和非叶子节点l满足 n+1 = l ,即n+l = len(arr) 所以最后一个非叶子节点下标为math.ceil((len(arr)-1)/2)-1
    # 将子节点中最大的和父节点比较，如果大于父节点则进行和父节点互换值，依次从下往上遍历父节点，最后，根节点是最大值。
    # 在数组中表示 非叶子节点为i，则子节点为2*i+1和2*i+2


    def build(a, length):

        index = math.ceil((length - 1) / 2) - 1

        for i in range(index, -1, -1):
            right = float("-inf")
            left = arr[2 * i + 1]  # 左子树是肯定有的
            if 2 * i + 2 < length:  # 有右子树  需要判断
                right = arr[2 * i + 2]
            if left <= right:
                if arr[i] < right:
                    arr[i], arr[2 * i + 2] = right, arr[i]
            else:
                if arr[i] < left:
                    arr[i], arr[2 * i + 1] = left, arr[i]



                    # 排序

    length = len(arr)
    build(arr, length)
    for i in range(length - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]

        length -= 1
        build(arr, length)


# 利用小顶堆进行降序排序
# 原理和大顶堆升序排序差不多，就是相反，父节点的值小于子节点的值，
# 1. 排序时，将最小的元素和最后一个子节点进行换位，继续2
# 2. 然后重新构建小顶堆，继续1

#                                  3                  6          7         8     19   //asc
# 8 6 7 19 3 - 》 3 6 8  7 19      - 》     6  8 7 19 - 》 7 8 19 -》 8 19 - 》19
def heapSortDes(arr):
    def build(a, length):

        index = math.ceil((length - 1) / 2) - 1

        for i in range(index, -1, -1):
            right = float("inf")  # 右子树初始化为无穷大值

            left = arr[2 * i + 1]  # 左子树是肯定有的
            if 2 * i + 2 < length:  # 有右子树  需要判断
                right = arr[2 * i + 2]
            if left >= right:
                if arr[i] > right:
                    arr[i], arr[2 * i + 2] = right, arr[i]
            else:
                if arr[i] > left:
                    arr[i], arr[2 * i + 1] = left, arr[i]



                    # 排序

    length = len(arr)
    build(arr, length)
    for i in range(length - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]

        length -= 1
        build(arr, length)


if __name__ == '__main__':
    arr = [6, 10, 13, 5, 8, 3, 2, 11, 18, 20, 17]

    arr3 = [6, 10, 13, 5, 8, 3, 2, 11, 18, 20, 17]

    quicksort3(arr3, 0, len(arr3)-1)
    print(arr3)
    quicksort(arr, 0, 8)
    print(arr)
    arr1 = [6, 5, 13, 5, 8, 3, 2, 11]
    quicksort2(arr1, 0, 8)
    print(arr1)

    arr2 = [70, 80, 60, 30, 50, 90, 20]
    heapSortAsc(arr2)
    print(arr2)
    arr3 = [70, 80, 60, 30, 50, 90, 20]
    heapSortDes(arr3)
    print(arr3)



    # n = 4000
    #
    # arr = []
    # for i in range(n):
    #     arr.append(random.randint(0,1000))
    #
    #
    #
    # print("原始数组",arr)
    # start1 = time.time()
    #
    # insertSort(arr.copy())
    #
    # print(time.time()-start1)
    # start2 = time.time()
    #
    # shellSort(arr.copy())
    #
    # print(time.time() - start2)
    #
    # start3 = time.time()
    #
    # selectionSort(arr.copy())
    #
    #
    # c = copy.deepcopy(arr)
    # print(time.time() - start3)
    #
    #
    # start4 = time.time()
    # arr4 = arr.copy()
    # mergeSort(arr4)
    #
    # print(time.time()-start4)
    #
    # start5 = time.time()
    # arr5 = arr.copy()
    #
    # arr5 = merge_sort(arr5)
    # print(time.time()-start5)
    # print(arr5)
    # print(arr4)
