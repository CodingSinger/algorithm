class Solution:
    # 思路：就是利用了快速排序的思想，设数组长度为l,我们知道快速排序每一次partition就会返回哨兵元素在数组中的位置r，如果r等于我们要找的k，则可以轻松找到第k小的元素了，即(l-k+1)大的元素。如果返回的r小于我们的k，
    # 因为我们知道分区后[0-l)之间的元素都小于arr[r]，(r-l)都大于arr[r]，所以我们继续partition区间[r,l)之间的元素有可能找到在位置k的哨兵。相反，如果r>k，则我们应该去区间[0,r)之间partition.重复上面的操作。到最后找到r==k

    def helper(self, arr, k):
        def partition(arr, s, e):

            guard = arr[s]

            temp = s  # temp相当于分割大于和小于guard的下标
            for i in range(s + 1, e):
                if arr[i] < guard:  # 找到一个比guard小的了，则guard的位置应该往后移一个位置。
                    temp += 1
                    arr[temp], arr[i] = arr[i], arr[temp]

            arr[s], arr[temp] = arr[temp], arr[s]  # guard回到属于自己应该在的位置

            return temp

        def select(arr, k):

            return sort(arr, 0, len(arr), k)

        def sort(arr, s, e, k):
            if s < e:
                r = partition(arr, s, e)
                if r > k:
                    return sort(arr, s, r, k)
                elif r < k:
                    return sort(arr, r + 1, e, k)
                else:
                    return arr[r]

            return -1

        return select(arr, k)

    # 最小堆 这里不再实现
    def helper2(self, arr, k):
        pass

    # 改进：因为我们知道在最坏的情况下，快速排序的时间复杂度为O(n^2),这是因为哨兵元素的每次取值都为分区区间的头或者尾部。BFPRT就是通过寻找均匀地哨兵元素，来降低TOP_K问题的时间复杂度。
    def helper3(self, arr, k):

        def insertSelection(arr, s, e):

            for i in range(s + 1, e+1):
                # num为将排序元素
                num = arr[i]
                # 遍历已排序元素
                for j in range(i - 1, s - 1, -1):
                    if arr[j] > num:
                        # 当前元素后移，为arr[i]留位置
                        arr[j + 1] = arr[j]
                        if j == s:  # 特殊判断 如果j已经到数组的最前面，则num需要插入到最前面
                            arr[j] = num
                    else:
                        # 插入到后面
                        arr[j + 1] = num
                        break

        # 获得数组的中位数
        def getMedian(arr, s, e):
            insertSelection(arr, s, e)
            x = s + e
            mid = x // 2 + x % 2
            return arr[mid]

        # 获得中位数的中位数
        def getMedianOfMidian(arr, s, e):

            # 首先需要分组
            if s == e:
                return arr[s]
            group = (e - s + 1) // 5
            if (e - s) // 5 != (e - s) / 5:
                group += 1

            begin = s-5
            medianArr = []
            for i in range(group):
                begin = begin+5
                end = begin+4
                if begin > e:
                    begin = e
                if end > e:
                    end = e
                medianArr.append(getMedian(arr, begin, end))

            return getMedianOfMidian(medianArr, 0, group - 1);

        def partition(arr, s, e):

            pivotIndex = getMedianOfMidian(arr, s, e)

            guard = arr[pivotIndex]
            temp = s

            # 重合时，退出循环
            while s < e:

                # 一定要从右边找起，从右边找到比哨兵小的
                while s < e and arr[e] >= guard:
                    e -= 1
                # 从左边找比哨兵大的
                while s < e and arr[s] <= guard:
                    s += 1

                # 交换大小
                if s < e:
                    arr[s], arr[e] = arr[e], arr[s]

            # 哨兵数归位
            arr[temp], arr[s] = arr[s], arr[temp]
            return s

        def select(arr, k):

            return sort(arr, 0, len(arr) - 1, k)

        def sort(arr, s, e, k):
            if s < e:
                r = partition(arr, s, e)
                if r > k:
                    return sort(arr, s, r, k)
                elif r < k:
                    return sort(arr, r + 1, e, k)
                else:
                    return arr[r]

            return -1

        return select(arr, k)


s = Solution()

arr = [15, 5, 8, 4, 7, 20, 16, 19]
# arr1 = arr
# arr[1] = 100
# k = 4
print(s.helper(arr, 6))
arr1 = [15, 5, 8, 4, 7, 20, 16, 19]
print(s.helper3(arr1, 2))
