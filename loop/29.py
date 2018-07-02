# 求数组中超过一半的数

# 思路：如果存在超过一半的数，则该数一定在排序之后的中位数,则我们只要判断中位数是否占有数组一半以上即可
# 那么核心问题就转化成如何最快得到中位数，全部排序取中间？如果数据量过大的话，这种方法是不可行的
# 该问题类似于求乱序大数组中的第k个元素，结合快排的元素定位+二分法 能够最大效率地找到某个位置的数
# 例如，要求第k个元素，先求出某个元素在有序数组的下标x,因此此时数组0-x之间都小于x的乱序元素，x-len(arr)是大于x的乱序元素集合，若该x小于k,则我们要求出的
# 第k个元素一定在0-x之间，否则在x-len(arr)之间，我们利用二分法不断缩小这个范围，最终找到第k个元素。


class Solution:
    def helper(self, arr):
        def quickSort(start, end):
            guard = arr[start]
            temp = start
            while start < end:

                while start < end and arr[end] >= guard:
                    end -= 1
                while start < end and arr[start] <= guard:
                    start += 1

                if start < end:
                    arr[end], arr[start] = arr[start], arr[end]

            arr[start], arr[temp] = arr[temp], arr[start]
            return start

        def handle(arr):

            mid = len(arr) >> 1
            start, end = 0, len(arr) - 1
            index = quickSort(0, end)
            while index != mid:
                if index < mid:
                    start = index + 1
                if index > mid:
                    end = index - 1

                index = quickSort(start, end)

            num = arr[index]

            return num if arr.count(num) > len(arr) >> 1 else -1

        return handle(arr)


s = Solution()
print(s.helper([2, 3, 5, 2, 2, 2, 3, 3, 3, 3, 3]))
